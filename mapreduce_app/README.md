# MapReduce Big Data Application

Aplicacao de processamento de dados usando o paradigma MapReduce, implementada em Python e containerizada com Docker.

Este diretorio foi preparado para execucao no GitHub Codespaces.

## Requisitos

- Python 3.8+
- Docker 20.10+
- Docker Compose 2+

## Executar com Python

```bash
cd mapreduce_app
python3 mapreduce_runner.py
```

Para processar outro arquivo:

```bash
python3 mapreduce_runner.py --input data/livro.txt --output data/livro_output.txt
```

## Executar com Docker

```bash
cd mapreduce_app
docker build -t mapreduce-app:v1.0 .
docker run --rm -v "$(pwd)/data:/app/data" mapreduce-app:v1.0
```

## Executar com Docker Compose

```bash
cd mapreduce_app
docker compose up --build mapreduce-processor
```

## Benchmark

```bash
cd mapreduce_app
python3 benchmark.py
```

O benchmark gera arquivos em `data/` e executa o pipeline para medir o tempo de processamento.

## Estrutura do Projeto

```text
mapreduce_app/
|-- mapper.py              # Fase Map: transforma texto em pares (palavra, 1)
|-- reducer.py             # Fase Reduce: agrega contagens por palavra
|-- mapreduce_runner.py    # Orquestrador do pipeline MapReduce
|-- benchmark.py           # Geracao de dados e medicao de desempenho
|-- Dockerfile             # Configuracao da imagem Docker
|-- docker-compose.yml     # Execucao containerizada local
|-- .dockerignore          # Arquivos ignorados no build Docker
`-- data/                  # Datasets e arquivos de saida
    |-- input.txt
    |-- logs.txt
    `-- livro.txt
```

## Como Funciona

O pipeline executado por `mapreduce_runner.py` segue este fluxo:

```text
arquivo de entrada -> mapper.py -> sort -> reducer.py -> arquivo de saida
```

1. **Map:** `mapper.py` le o texto e emite pares `palavra<TAB>1`.
2. **Shuffle & Sort:** o comando `sort` organiza os pares por palavra.
3. **Reduce:** `reducer.py` soma as contagens de cada palavra.

## Comandos Uteis

Ver as palavras mais frequentes:

```bash
sort -t$'\t' -k2 -nr data/output.txt | head -20
```

Consultar palavras especificas no resultado de Dom Casmurro:

```bash
grep -E $'^(capitú|bentinho|amor|ciume)\t' data/livro_output.txt
```

## Troubleshooting

Se o Docker nao responder no Codespaces, verifique:

```bash
docker --version
docker info
```

Se o arquivo de saida nao aparecer, confirme que voce esta no diretorio `mapreduce_app` e que o arquivo de entrada existe:

```bash
pwd
ls -la data
```

## Recursos

- [MapReduce Paper - Google](https://research.google/pubs/pub62/)
- [Docker Documentation](https://docs.docker.com/)
- [GitHub Codespaces Documentation](https://docs.github.com/codespaces)
