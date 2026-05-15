#!/usr/bin/env python3
"""
Mapper: Transforma linhas de texto em pares (palavra, 1)
Ignorando stopwords
"""

import sys
import re
from stopwords import STOPWORDS


def mapper():
    """
    Lê linhas do stdin e emite pares (palavra, 1)
    ignorando palavras irrelevantes.
    """

    for line in sys.stdin:

        # Remove espaços e converte para minúsculas
        line = line.strip().lower()

        # Extrai palavras
        words = re.findall(r'\b\w+\b', line)

        # Emite apenas palavras úteis
        for word in words:

            if word not in STOPWORDS:
                print(f"{word}\t1")


if __name__ == "__main__":
    mapper()