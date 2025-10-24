#!/usr/bin/env python3
"""
Reducer: Agrega contagens de palavras
"""
import sys
from collections import defaultdict

def reducer():
    """
    Lê pares (palavra, contagem) do stdin e soma as contagens
    """
    word_counts = defaultdict(int)
    
    for line in sys.stdin:
        # Remove espaços em branco
        line = line.strip()
        
        # Divide a linha em palavra e contagem
        try:
            word, count = line.split('\t')
            word_counts[word] += int(count)
        except ValueError:
            # Ignora linhas mal formatadas
            continue
    
    # Emite resultados ordenados
    for word in sorted(word_counts.keys()):
        print(f"{word}\t{word_counts[word]}")

if __name__ == "__main__":
    reducer()
