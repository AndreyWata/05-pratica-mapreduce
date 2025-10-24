# Imagem base Python
FROM python:3.11-slim

# Metadata
LABEL maintainer="estudante@cienciadados.edu"
LABEL description="MapReduce Application for Big Data Processing"

# Define diretório de trabalho
WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    coreutils && \
    rm -rf /var/lib/apt/lists/*

# Copia os scripts Python
COPY mapper.py reducer.py mapreduce_runner.py ./

# Cria diretório para dados
RUN mkdir -p /app/data

# Torna scripts executáveis
RUN chmod +x mapper.py reducer.py mapreduce_runner.py

# Define o comando padrão
CMD ["python3", "mapreduce_runner.py"]
