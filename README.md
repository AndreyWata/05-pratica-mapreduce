# Atividade Pratica: MapReduce com Python, Docker e GitHub Codespaces

## Informacoes Gerais

**Publico-alvo:** alunos de graduacao em Ciencia de Dados  
**Tematica:** infraestrutura para projetos de Big Data  
**Nivel:** intermediario  
**Ambiente obrigatorio:** GitHub Codespaces

---

## Objetivos de Aprendizagem

Ao final desta atividade, voce sera capaz de:

1. Explicar os fundamentos do paradigma MapReduce.
2. Implementar as fases Map, Shuffle/Sort e Reduce em Python.
3. Executar uma aplicacao de processamento de dados no GitHub Codespaces.
4. Containerizar a aplicacao com Docker e executar o processamento em container.
5. Analisar resultados de contagem de palavras em datasets pequenos e maiores.
6. Registrar evidencias tecnicas da execucao da atividade.

---

## Pre-requisitos

- Conhecimento basico de Python.
- Familiaridade com terminal Linux.
- Conta no GitHub.
- Navegador web moderno.

> Toda a atividade deve ser executada no GitHub Codespaces. Nao utilize ambientes externos ou descontinuados.

---

## Recursos Necessarios

- **GitHub Codespaces**: ambiente de desenvolvimento em nuvem com terminal, editor, Python e Docker.
- **Repositorio da atividade**: fornecido pelo professor.
- **Datasets locais**: arquivos em `mapreduce_app/data/`.

---

## Parte 1: Revisao Teorica sobre MapReduce

### 1.1 O que e MapReduce?

MapReduce e um modelo de programacao criado para processar grandes volumes de dados por meio de tarefas independentes, paralelizaveis e distribuidas. A ideia central e quebrar um problema grande em partes menores, processar essas partes separadamente e depois combinar os resultados.

Esse paradigma foi popularizado pelo Google e influenciou ferramentas de Big Data como Hadoop. Mesmo quando usado em uma simulacao local, como nesta atividade, ele ajuda a entender como sistemas distribuidos organizam dados, trabalho e agregacao de resultados.

### 1.2 Fases do processamento

O fluxo classico de MapReduce possui tres momentos principais:

1. **Map**: recebe dados brutos e transforma cada item de entrada em pares chave-valor.
2. **Shuffle & Sort**: agrupa os valores que possuem a mesma chave e ordena os dados para facilitar a agregacao.
3. **Reduce**: recebe cada chave com seus valores associados e calcula o resultado final.

Fluxo conceitual:

```text
Entrada -> Split -> Map -> Shuffle & Sort -> Reduce -> Saida
```

### 1.3 Exemplo: contagem de palavras

Entrada:

```text
big data
data science
big systems
```

Saida da fase Map:

```text
big     1
data    1
data    1
science 1
big     1
systems 1
```

Depois do Shuffle & Sort:

```text
big     [1, 1]
data    [1, 1]
science [1]
systems [1]
```

Saida da fase Reduce:

```text
big     2
data    2
science 1
systems 1
```

### 1.4 Por que MapReduce e importante em Big Data?

MapReduce e importante porque permite:

- **Paralelismo:** diferentes partes do dataset podem ser processadas ao mesmo tempo.
- **Escalabilidade:** o mesmo modelo pode ser executado em poucos arquivos ou em grandes clusters.
- **Tolerancia a falhas:** em plataformas distribuidas, tarefas com erro podem ser reexecutadas.
- **Separacao de responsabilidades:** a funcao Map transforma dados; a funcao Reduce agrega resultados.
- **Processamento em lote:** o modelo e adequado para tarefas analiticas sobre grandes volumes de dados historicos.

### 1.5 Limitacoes do modelo

MapReduce nao e ideal para todos os cenarios. Ele pode ser menos eficiente quando:

- O processamento precisa ser interativo ou em tempo real.
- O algoritmo exige muitas iteracoes sucessivas sobre os mesmos dados.
- Ha necessidade de baixa latencia.
- O custo de escrita e leitura intermediaria e alto.

Frameworks mais recentes, como Apache Spark, surgiram para reduzir algumas dessas limitacoes, mas MapReduce continua sendo uma base conceitual importante para entender Big Data.

### Checkpoint 1

Antes de prosseguir, confirme:

- [ ] Sei explicar a diferenca entre Map e Reduce.
- [ ] Entendo o papel da fase Shuffle & Sort.
- [ ] Consigo descrever por que pares chave-valor sao usados.
- [ ] Reconheco vantagens e limitacoes do MapReduce.

---

## Parte 2: Configuracao do Ambiente no GitHub Codespaces

### 2.1 Criando o ambiente

1. Acesse o repositorio original fornecido pelo professor.
2. Clique em **Fork** para criar uma copia na sua conta.
3. No seu fork, clique em **Code**.
4. Abra a aba **Codespaces**.
5. Clique em **Create codespace on main**.
6. Aguarde o ambiente carregar.

### 2.2 Verificando ferramentas

No terminal do Codespaces, execute:

```bash
python3 --version
docker --version
docker compose version
```

### 2.3 Explorando o projeto

```bash
ls -la
ls -la mapreduce_app
```

Arquivos principais:

- `mapper.py`: implementa a fase Map.
- `reducer.py`: implementa a fase Reduce.
- `mapreduce_runner.py`: orquestra o pipeline completo.
- `benchmark.py`: gera datasets de teste e mede desempenho.
- `Dockerfile`: define a imagem da aplicacao.
- `docker-compose.yml`: executa a aplicacao containerizada.
- `data/`: contem os datasets usados na atividade.

### Checkpoint 2

- [ ] O Codespace abriu corretamente.
- [ ] Python esta disponivel.
- [ ] Docker esta disponivel.
- [ ] Os arquivos da aplicacao estao visiveis.

---

## Parte 3: Implementacao MapReduce em Python

### 3.1 Entrando no diretorio da aplicacao

```bash
cd mapreduce_app
```

### 3.2 Entendendo o dataset inicial

```bash
cat data/input.txt
```

Esse arquivo contem frases curtas sobre Big Data e tecnologia. Ele sera usado para validar o pipeline antes de processar arquivos maiores.

### 3.3 Analisando o Mapper

```bash
cat mapper.py
```

O `mapper.py`:

- Le linhas de texto da entrada padrao.
- Converte o texto para minusculas.
- Extrai palavras usando expressao regular.
- Emite pares no formato `palavra<TAB>1`.

Teste isolado do mapper:

```bash
echo "Big data, big systems" | python3 mapper.py
```

### 3.4 Analisando o Reducer

```bash
cat reducer.py
```

O `reducer.py`:

- Le pares `palavra<TAB>contagem`.
- Soma as contagens por palavra.
- Emite o resultado final ordenado alfabeticamente.

Teste isolado do reducer:

```bash
printf "big\t1\nbig\t1\ndata\t1\n" | python3 reducer.py
```

### 3.5 Entendendo o Runner

```bash
cat mapreduce_runner.py
```

O `mapreduce_runner.py` executa o pipeline completo:

```text
arquivo de entrada -> mapper.py -> sort -> reducer.py -> arquivo de saida
```

Ele tambem mostra estatisticas e as 10 palavras mais frequentes.

### 3.6 Executando o pipeline

```bash
python3 mapreduce_runner.py
```

Visualize a saida:

```bash
cat data/output.txt
```

### Checkpoint 3

- [ ] O pipeline executou sem erros.
- [ ] O arquivo `data/output.txt` foi criado.
- [ ] As palavras foram contadas corretamente.
- [ ] O terminal exibiu estatisticas e top 10 palavras.

---

## Parte 4: Containerizacao com Docker

### 4.1 Explorando o Dockerfile

```bash
cat Dockerfile
```

Pontos principais:

- `FROM python:3.11-slim`: usa uma imagem base leve com Python.
- `WORKDIR /app`: define o diretorio de trabalho no container.
- `apt-get install coreutils`: garante o comando `sort`.
- `COPY`: copia os scripts para a imagem.
- `CMD`: define o comando padrao do container.

### 4.2 Verificando o .dockerignore

```bash
cat .dockerignore
```

Esse arquivo evita enviar conteudos desnecessarios para o contexto de build.

### 4.3 Construindo a imagem

```bash
docker build -t mapreduce-app:v1.0 .
```

### 4.4 Verificando a imagem local

```bash
docker images | grep mapreduce-app
```

### Checkpoint 4

- [ ] Entendi a estrutura do `Dockerfile`.
- [ ] A imagem `mapreduce-app:v1.0` foi criada.
- [ ] A imagem aparece na listagem local do Docker.

---

## Parte 5: Executando a Aplicacao Containerizada

### 5.1 Executando o container

No Codespaces, dentro do diretorio `mapreduce_app`, execute:

```bash
docker run --rm \
  -v "$(pwd)/data:/app/data" \
  mapreduce-app:v1.0
```

Verifique o resultado:

```bash
cat data/output.txt
```

### 5.2 Executando com Docker Compose

```bash
docker compose up --build mapreduce-processor
```

### 5.3 Benchmark

Execute o benchmark localmente:

```bash
python3 benchmark.py
```

O script cria arquivos de 1 MB, 5 MB e 10 MB em `data/` e mede o tempo de processamento.

### 5.4 Processando um arquivo gerado pelo benchmark no container

Depois de executar o benchmark, processe um arquivo maior:

```bash
docker run --rm \
  -v "$(pwd)/data:/app/data" \
  mapreduce-app:v1.0 \
  python3 mapreduce_runner.py --input data/benchmark_1mb.txt --output data/benchmark_1mb_output.txt
```

### Checkpoint 5

- [ ] O container executou sem erros.
- [ ] O volume `data/` foi montado corretamente.
- [ ] O benchmark gerou arquivos de teste.
- [ ] Um arquivo maior foi processado com sucesso.

---

## Parte 6: Exercicio Pratico - Analise Literaria

O arquivo `data/livro.txt` contem o texto de **Dom Casmurro**, de Machado de Assis, disponibilizado pelo Projeto Gutenberg.

Use MapReduce para analisar:

- Palavras mais frequentes no texto.
- Ocorrencias de termos como `capitu`, `bentinho`, `amor` e `ciume`.
- Termos que aparecem com maior recorrencia na obra.

### 6.1 Visualizando uma amostra

```bash
head -n 50 data/livro.txt
```

### 6.2 Processando o livro

```bash
python3 mapreduce_runner.py --input data/livro.txt --output data/livro_output.txt
```

### 6.3 Analisando as palavras mais frequentes

```bash
sort -t$'\t' -k2 -nr data/livro_output.txt | head -20
```

### 6.4 Consultando palavras especificas

```bash
grep -E $'^(capitu|bentinho|amor|ciume)\t' data/livro_output.txt
```

> Observacao: o mapper converte palavras para minusculas. Por isso, pesquise por `capitu`, e nao `Capitu`.

### Evidencias obrigatorias

Capture evidencias da execucao:

- Screenshot do terminal mostrando o processamento de `data/livro.txt`.
- Screenshot do top 20 de palavras mais frequentes.
- Registro textual informando quantas vezes `capitu` aparece no arquivo processado.

### Checkpoint 6

- [ ] O livro foi processado com sucesso.
- [ ] O arquivo `data/livro_output.txt` foi criado.
- [ ] As palavras mais frequentes foram analisadas.
- [ ] A frequencia de `capitu` foi identificada.
- [ ] As evidencias foram capturadas.

---

## Parte 7: Registro no GitHub

Ao final da atividade, registre suas alteracoes no seu fork:

```bash
git status
git add .
git commit -m "conclui atividade mapreduce"
git push
```

Se o Git solicitar configuracao de usuario no Codespaces, execute:

```bash
git config user.name "Seu Nome"
git config user.email "seu-email@example.com"
```

Depois repita o commit.

### Checkpoint 7

- [ ] Os resultados e alteracoes foram revisados com `git status`.
- [ ] O commit foi criado.
- [ ] O push foi enviado para o fork.

---

## Parte 8: Entrega da Atividade

Entregue as evidencias na plataforma Microsoft Teams, conforme orientacao do professor.

### Evidencias obrigatorias

1. **Execucao no Codespaces**
   - Screenshot do terminal com `python3 --version` e `docker --version`.
   - Screenshot mostrando o repositorio aberto no Codespaces.

2. **Processamento MapReduce**
   - Screenshot da execucao de `python3 mapreduce_runner.py`.
   - Screenshot do arquivo `data/output.txt`.

3. **Container Docker**
   - Screenshot do comando `docker build -t mapreduce-app:v1.0 .`.
   - Screenshot do comando `docker run` executado com sucesso.

4. **Analise de Dom Casmurro**
   - Screenshot da execucao com `data/livro.txt`.
   - Screenshot do top 20 de palavras.
   - Resposta textual: quantas vezes a palavra `capitu` aparece?

5. **Repositorio**
   - Link do seu fork no GitHub.

---

## Checkpoint Final

Autoavaliacao:

- [ ] Compreendo o paradigma MapReduce.
- [ ] Consigo explicar Map, Shuffle/Sort e Reduce.
- [ ] Sei executar a aplicacao no Codespaces.
- [ ] Sei construir e executar uma imagem Docker local.
- [ ] Consigo interpretar os resultados da contagem de palavras.
- [ ] Tenho evidencias suficientes para entregar a atividade.

---

## Recursos Adicionais

- [MapReduce Paper - Google](https://research.google/pubs/pub62/)
- [Docker Documentation](https://docs.docker.com/)
- [GitHub Codespaces Documentation](https://docs.github.com/codespaces)
- [Python subprocess module](https://docs.python.org/3/library/subprocess.html)

---

## Conclusao

Nesta atividade, voce revisou a teoria de MapReduce, executou um pipeline de contagem de palavras em Python, containerizou a aplicacao com Docker e analisou um texto literario usando o ambiente GitHub Codespaces.
