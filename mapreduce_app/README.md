# MapReduce Big Data Application

Aplicação de processamento de dados usando o paradigma MapReduce, implementada em Python e containerizada com Docker.

## 🚀 Quick Start

### Requisitos
- Python 3.8+
- Docker 20.10+ (opcional, para containerização)
- Docker Compose 2.0+ (opcional, para orquestração)

### Executar Localmente

```bash
# Navegue até o diretório da aplicação
cd mapreduce_app

# Torne os scripts executáveis (Linux/Mac)
chmod +x mapper.py reducer.py mapreduce_runner.py

# Execute o processamento
python3 mapreduce_runner.py
```

### Executar com Docker

```bash
# Construa a imagem
docker build -t mapreduce-app:v1.0 .

# Execute o container
docker run --rm -v "$(pwd)/data:/app/data" mapreduce-app:v1.0
```

### Executar com Docker Compose

```bash
# Processamento padrão
docker-compose up mapreduce-processor

# Processamento de arquivo grande
docker-compose --profile large up mapreduce-large
```

## 📊 Estrutura do Projeto

```
mapreduce_app/
├── mapper.py              # Função Map - transforma texto em pares (palavra, 1)
├── reducer.py             # Função Reduce - agrega contagens de palavras
├── mapreduce_runner.py    # Orquestrador do pipeline MapReduce
├── benchmark.py           # Script de análise de desempenho
├── Dockerfile             # Configuração da imagem Docker
├── docker-compose.yml     # Orquestração de containers
├── .dockerignore          # Arquivos ignorados pelo Docker
└── data/                  # Datasets de exemplo
    ├── input.txt          # Dataset pequeno para testes
    └── logs.txt           # Dataset de logs para exercícios
```

## 🧪 Testes e Benchmark

```bash
# Execute o benchmark de desempenho
python3 benchmark.py
```

## 📝 Como Funciona

### Pipeline MapReduce

1. **Map**: O `mapper.py` lê linhas de texto e emite pares `(palavra, 1)` para cada palavra encontrada
2. **Shuffle & Sort**: As palavras são ordenadas alfabeticamente (usando o comando `sort`)
3. **Reduce**: O `reducer.py` agrega as contagens de cada palavra

### Exemplo de Execução

**Entrada (input.txt):**
```
big data is transforming the world
data science requires big data infrastructure
```

**Saída do Map:**
```
big	1
data	1
is	1
transforming	1
...
```

**Saída do Reduce:**
```
big	2
data	3
infrastructure	1
...
```

## 🎓 Exercícios Práticos

### Exercício 1: Análise de Logs
Modifique os scripts para contar logs por tipo (INFO, WARNING, ERROR) usando o arquivo `data/logs.txt`.

### Exercício 2: Top-K Palavras
Altere o reducer para retornar apenas as K palavras mais frequentes.

### Exercício 3: Análise de Sentimentos
Implemente um classificador simples de sentimentos (positivo/negativo/neutro).

## 🔧 Customização

### Processar arquivo diferente

```bash
python3 mapreduce_runner.py --input data/seu_arquivo.txt --output data/resultado.txt
```

### Gerar arquivo de teste grande

```python
python3 << 'EOF'
import random

words = ["data", "big", "python", "docker", "mapreduce", "science"]
with open("data/large_input.txt", "w") as f:
    for _ in range(1000):
        line = " ".join(random.choices(words, k=15))
        f.write(line + "\n")
EOF
```

## 📚 Recursos de Aprendizagem

- [MapReduce Paper (Google)](https://research.google/pubs/pub62/)
- [Docker Documentation](https://docs.docker.com/)
- [Apache Hadoop](https://hadoop.apache.org/)
- [Apache Spark](https://spark.apache.org/)

## 🐛 Troubleshooting

### Erro: Permissão negada
```bash
chmod +x mapper.py reducer.py mapreduce_runner.py
```

### Erro: Comando 'sort' não encontrado (Windows)
No Windows, use o Git Bash ou WSL para executar os scripts.

### Erro: Volume não montado no Docker (Windows)
```bash
docker run --rm -v "${PWD}/data:/app/data" mapreduce-app:v1.0
```

## 📄 Licença

MIT License - Livre para uso educacional e comercial.

---

**Desenvolvido para o curso de Ciência de Dados**  
**Versão 1.0 - Outubro 2025**
