#!/usr/bin/env python3
"""
Benchmark para análise de desempenho do MapReduce
"""
import time
import subprocess
import os
from pathlib import Path

def generate_test_file(size_mb, filename):
    """Gera arquivo de teste com tamanho específico"""
    words = ["data", "big", "python", "docker", "mapreduce"] * 100
    
    target_size = size_mb * 1024 * 1024  # Converte MB para bytes
    current_size = 0
    
    with open(filename, 'w') as f:
        while current_size < target_size:
            line = " ".join(words[:50]) + "\n"
            f.write(line)
            current_size += len(line.encode('utf-8'))
    
    actual_size = os.path.getsize(filename) / (1024 * 1024)
    print(f"✅ Arquivo gerado: {filename} ({actual_size:.2f} MB)")

def run_benchmark(input_file, output_file):
    """Executa benchmark e mede tempo"""
    start_time = time.time()
    
    result = subprocess.run(
        ['python3', 'mapreduce_runner.py', '--input', input_file, '--output', output_file],
        capture_output=True,
        text=True
    )
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    return elapsed_time, result.returncode == 0

def main():
    print("🔬 Iniciando Benchmark do MapReduce\n")
    
    test_sizes = [1, 5, 10]  # Tamanhos em MB
    results = []
    
    for size in test_sizes:
        filename = f"data/benchmark_{size}mb.txt"
        output = f"data/benchmark_{size}mb_output.txt"
        
        print(f"\n📊 Teste com {size} MB de dados:")
        generate_test_file(size, filename)
        
        elapsed, success = run_benchmark(filename, output)
        
        if success:
            throughput = size / elapsed if elapsed > 0 else 0
            results.append((size, elapsed, throughput))
            print(f"⏱️  Tempo: {elapsed:.2f}s")
            print(f"🚀 Throughput: {throughput:.2f} MB/s")
        else:
            print("❌ Falha no processamento")
    
    print("\n" + "="*50)
    print("📈 RESUMO DOS RESULTADOS")
    print("="*50)
    for size, elapsed, throughput in results:
        print(f"{size:>3} MB | {elapsed:>6.2f}s | {throughput:>6.2f} MB/s")

if __name__ == "__main__":
    main()
