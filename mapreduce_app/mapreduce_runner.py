#!/usr/bin/env python3
"""
MapReduce Runner: Orquestra o pipeline Map-Reduce em Python puro
"""

import sys
import re
import argparse
from pathlib import Path
from collections import defaultdict

from stopwords import STOPWORDS


def run_map_phase(input_file):
    """
    Fase MAP:
    lê o arquivo e emite pares (palavra, 1),
    ignorando stopwords.
    """

    pairs = []

    with open(input_file, 'r', encoding='utf-8') as f:

        for line in f:

            # Padroniza texto
            line = line.strip().lower()

            # Extrai palavras
            words = re.findall(r'\b\w+\b', line)

            # Adiciona apenas palavras relevantes
            for word in words:

                if word not in STOPWORDS:
                    pairs.append((word, 1))

    return pairs


def run_shuffle_sort(pairs):
    """
    Fase Shuffle & Sort:
    ordena os pares pela chave (palavra).
    """

    return sorted(pairs, key=lambda x: x[0])


def run_reduce_phase(sorted_pairs):
    """
    Fase Reduce:
    soma as contagens de cada palavra.
    """

    word_counts = defaultdict(int)

    for word, count in sorted_pairs:
        word_counts[word] += count

    return dict(word_counts)


def run_mapreduce(input_file, output_file):
    """
    Executa o pipeline MapReduce completo.
    """

    print("Iniciando processamento MapReduce...")
    print(f"Input:  {input_file}")
    print(f"Output: {output_file}")

    if not Path(input_file).exists():
        print(f"Erro: arquivo '{input_file}' nao encontrado.")
        sys.exit(1)

    # MAP
    print("\nFase 1: MAP - processando palavras...")
    pairs = run_map_phase(input_file)

    # SHUFFLE & SORT
    print("Fase 2: SHUFFLE & SORT - ordenando dados...")
    sorted_pairs = run_shuffle_sort(pairs)

    # REDUCE
    print("Fase 3: REDUCE - agregando resultados...")
    word_counts = run_reduce_phase(sorted_pairs)

    # Salva saída
    with open(output_file, 'w', encoding='utf-8') as f:

        for word in sorted(word_counts.keys()):
            f.write(f"{word}\t{word_counts[word]}\n")

    print(f"\nProcessamento concluido.")
    print(f"Resultados em: {output_file}")

    print(f"\nTotal de palavras unicas: {len(word_counts)}")

    # Top 10
    print("\nTop 10 palavras mais frequentes:")

    top10 = sorted(
        word_counts.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]

    for i, (word, count) in enumerate(top10, 1):
        print(f"  {i:2}. {word}: {count}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='MapReduce Word Count'
    )

    parser.add_argument(
        '--input',
        default='data/input.txt',
        help='Arquivo de entrada'
    )

    parser.add_argument(
        '--output',
        default='data/output.txt',
        help='Arquivo de saida'
    )

    args = parser.parse_args()

    run_mapreduce(args.input, args.output)