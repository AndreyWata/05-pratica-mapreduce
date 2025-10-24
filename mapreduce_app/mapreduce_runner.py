#!/usr/bin/env python3
"""
MapReduce Runner: Orquestra o pipeline Map-Reduce
"""
import subprocess
import sys
from pathlib import Path
import argparse

def run_mapreduce(input_file, output_file):
    """
    Executa o pipeline MapReduce completo
    
    Args:
        input_file: Caminho do arquivo de entrada
        output_file: Caminho do arquivo de saída
    """
    print("🚀 Iniciando processamento MapReduce...")
    print(f"📂 Input: {input_file}")
    print(f"📂 Output: {output_file}")
    
    # Verifica se o arquivo de entrada existe
    if not Path(input_file).exists():
        print(f"❌ Erro: Arquivo {input_file} não encontrado!")
        sys.exit(1)
    
    try:
        # Fase MAP
        print("📍 Fase 1: MAP - Processando palavras...")
        with open(input_file, 'r') as f_in:
            map_process = subprocess.Popen(
                ['python3', 'mapper.py'],
                stdin=f_in,
                stdout=subprocess.PIPE,
                text=True
            )
        
        # Fase SORT (simulando shuffle)
        print("📍 Fase 2: SHUFFLE & SORT - Organizando dados...")
        sort_process = subprocess.Popen(
            ['sort'],
            stdin=map_process.stdout,
            stdout=subprocess.PIPE,
            text=True
        )
        map_process.stdout.close()
        
        # Fase REDUCE
        print("📍 Fase 3: REDUCE - Agregando resultados...")
        with open(output_file, 'w') as f_out:
            reduce_process = subprocess.Popen(
                ['python3', 'reducer.py'],
                stdin=sort_process.stdout,
                stdout=f_out,
                text=True
            )
            sort_process.stdout.close()
            reduce_process.wait()
        
        print(f"✅ Processamento concluído! Resultados em: {output_file}")
        
        # Exibe estatísticas
        with open(output_file, 'r') as f:
            lines = f.readlines()
            print(f"📊 Total de palavras únicas: {len(lines)}")
            
        # Exibe top 10 palavras mais frequentes
        print("\n🏆 Top 10 palavras mais frequentes:")
        sorted_words = sorted(lines, key=lambda x: int(x.split('\t')[1]), reverse=True)
        for i, line in enumerate(sorted_words[:10], 1):
            word, count = line.strip().split('\t')
            print(f"   {i}. {word}: {count}")
            
    except Exception as e:
        print(f"❌ Erro durante o processamento: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='MapReduce Word Count')
    parser.add_argument('--input', default='data/input.txt', 
                       help='Arquivo de entrada')
    parser.add_argument('--output', default='data/output.txt', 
                       help='Arquivo de saída')
    
    args = parser.parse_args()
    run_mapreduce(args.input, args.output)
