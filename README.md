# Atividade Prática: MapReduce com Python e Docker

## Informações Gerais

**Público-alvo:** Alunos de graduação em Ciência de Dados  
**Temática:** Infraestrutura para projetos de Big Data  
**Nível:** Intermediário

---

## Objetivos de Aprendizagem

Ao final desta atividade, você será capaz de:

1. Compreender os conceitos fundamentais do paradigma MapReduce
2. Implementar funções Map e Reduce em Python
3. Containerizar aplicações de Big Data usando Docker
4. Processar datasets de forma distribuída
5. Aplicar boas práticas de infraestrutura para projetos de dados

---

## Pré-requisitos

- Conhecimento básico de Python
- Familiaridade com linha de comando (terminal/bash)
- Conta no GitHub (gratuita)
- Conta no Docker Hub (gratuita)
- Navegador web moderno

---

## Recursos Necessários

Todos os recursos podem ser acessados online gratuitamente:

- **GitHub Codespaces** (ambiente de desenvolvimento na nuvem)
- **Play with Docker** (https://labs.play-with-docker.com/) - Ambiente Docker online
- **Dataset**: Arquivo de texto com dados para processamento

---

## Parte 1: Fundamentos do MapReduce

### 1.1 Conceitos Teóricos

#### O que é MapReduce?

MapReduce é um modelo de programação para processamento de grandes volumes de dados de forma distribuída e paralela. Foi popularizado pelo Google e é a base de frameworks como Hadoop.

**Componentes principais:**

1. **Map (Mapeamento)**: Transforma dados de entrada em pares chave-valor
2. **Shuffle & Sort**: Agrupa todos os valores associados à mesma chave
3. **Reduce (Redução)**: Processa e agrega os valores agrupados

**Fluxo de execução:**

```
Input → Split → Map → Shuffle & Sort → Reduce → Output
```

#### Exemplo Conceitual: Contagem de Palavras

**Entrada:**
```
"hello world"
"hello python"
```

**Fase Map:**
```
("hello", 1)
("world", 1)
("hello", 1)
("python", 1)
```

**Fase Shuffle & Sort:**
```
("hello", [1, 1])
("python", [1])
("world", [1])
```

**Fase Reduce:**
```
("hello", 2)
("python", 1)
("world", 1)
```

### ✅ Checkpoint 1.1

Antes de prosseguir, responda:

- [ ] Você compreende a diferença entre Map e Reduce?
- [ ] Você consegue explicar o que acontece na fase Shuffle & Sort?
- [ ] Você entende por que MapReduce é adequado para Big Data?

---

## Parte 2: Configuração do Ambiente

### 2.1 Fazendo Fork e Clonando o Repositório no GitHub Codespaces

**Passo 1:** Acesse https://github.com e faça login

**Passo 2:** Faça um fork do repositório do laboratório

1. Acesse o repositório original fornecido pelo professor
2. Clique no botão "Fork" no canto superior direito
3. Selecione sua conta como destino do fork
4. Aguarde a criação do fork (alguns segundos)

**Passo 3:** Clone seu fork usando GitHub Codespaces

1. No seu fork, clique no botão verde "Code"
2. Selecione a aba "Codespaces"
3. Clique em "Create codespace on main"
4. Aguarde o ambiente carregar (pode levar 1-2 minutos)

**Passo 4:** Verifique o ambiente

```bash
python3 --version
docker --version
```

**Passo 5:** Explore a estrutura do projeto

```bash
ls -la mapreduce_app/
```

Você verá:
- `mapper.py` - Script de mapeamento
- `reducer.py` - Script de redução
- `mapreduce_runner.py` - Orquestrador principal
- `benchmark.py` - Script de análise de desempenho
- `Dockerfile` - Configuração do container
- `data/` - Diretório com datasets de exemplo

### ✅ Checkpoint 2.1

Verifique:

- [ ] Fork do repositório foi criado com sucesso
- [ ] Repositório foi clonado no Codespaces
- [ ] Python 3.x está instalado
- [ ] Docker está disponível
- [ ] Todos os arquivos da aplicação estão presentes
- [ ] Você consegue visualizar os scripts Python

---

## Parte 3: Implementação do MapReduce em Python

### 3.1 Explorando a Estrutura do Projeto

O repositório já contém todos os scripts necessários. Vamos entender cada componente:

```bash
cd mapreduce_app
ls -la
```

Você verá a seguinte estrutura:

```
mapreduce_app/
├── mapper.py              # Função Map
├── reducer.py             # Função Reduce  
├── mapreduce_runner.py    # Orquestrador
├── benchmark.py           # Análise de desempenho
├── Dockerfile             # Imagem Docker
├── .dockerignore          # Arquivos ignorados
└── data/                  # Datasets
    ├── input.txt          # Dataset de exemplo
    └── livro.txt          # Dom Casmurro (Projeto Gutenberg)
```

### 3.2 Entendendo o Dataset

Visualize o conteúdo do arquivo de entrada:

```bash
cat data/input.txt
```

O arquivo contém frases sobre Big Data e tecnologia que serão processadas pelo MapReduce.

### 3.3 Analisando o Mapper

Abra e analise o arquivo `mapper.py`:

```bash
cat mapper.py
```

**O que o Mapper faz:**
- Lê linhas de texto da entrada padrão (stdin)
- Converte o texto para minúsculas
- Remove pontuação usando expressões regulares
- Emite cada palavra no formato `palavra\t1`

**Conceitos importantes:**
- Usa `sys.stdin` para ler dados
- Usa `re.findall()` para extrair palavras
- Emite pares chave-valor no formato TSV (Tab-Separated Values)

### 3.4 Analisando o Reducer

Abra e analise o arquivo `reducer.py`:

```bash
cat reducer.py
```

**O que o Reducer faz:**
- Lê pares `palavra\tcontagem` da entrada padrão
- Usa `defaultdict` para acumular contagens
- Emite resultados ordenados alfabeticamente

**Conceitos importantes:**
- Pressupõe que a entrada já está ordenada (fase Shuffle & Sort)
- Usa estruturas de dados eficientes (`defaultdict`)
- Tratamento de erros para linhas mal formatadas

### 3.5 Analisando o Runner (Orquestrador)

Abra e analise o arquivo `mapreduce_runner.py`:

```bash
cat mapreduce_runner.py
```

**O que o Runner faz:**
1. Orquestra todo o pipeline MapReduce
2. Executa os 3 processos em sequência usando `subprocess`
3. Conecta a saída de um processo na entrada do próximo (pipes)
4. Exibe estatísticas e top 10 palavras mais frequentes

**Conceitos importantes:**
- Usa `subprocess.Popen()` para criar processos
- Implementa pipeline Unix: `cat file | python3 mapper.py | sort | python3 reducer.py`
- Aceita argumentos de linha de comando (`--input`, `--output`)

### 3.6 Testando a Implementação

Execute o processamento MapReduce:

### 3.6 Testando a Implementação

Execute o processamento MapReduce:

```bash
# Torne os scripts executáveis (Linux/Mac/Git Bash)
chmod +x mapper.py reducer.py mapreduce_runner.py

# Execute o runner
python3 mapreduce_runner.py
```

Visualize os resultados:

```bash
cat data/output.txt
```

### ✅ Checkpoint 3.6

Verifique:

- [ ] Você entendeu o propósito de cada script
- [ ] O processamento foi executado com sucesso
- [ ] O arquivo `data/output.txt` foi gerado
- [ ] Você consegue ver a contagem de palavras
- [ ] As palavras "data" e "big" aparecem múltiplas vezes
- [ ] As estatísticas e top 10 foram exibidas corretamente

---

## Parte 4: Containerização com Docker

### 4.1 Explorando o Dockerfile

O repositório já contém um `Dockerfile` configurado. Vamos entender seu conteúdo:

```bash
cat Dockerfile
```

**Componentes do Dockerfile:**

- `FROM python:3.11-slim` - Imagem base leve do Python
- `WORKDIR /app` - Define o diretório de trabalho
- `RUN apt-get update...` - Instala dependências do sistema (comando `sort`)
- `COPY` - Copia os scripts Python para o container
- `RUN chmod +x` - Torna os scripts executáveis
- `CMD` - Comando padrão ao executar o container

### 4.2 Verificando o .dockerignore

O arquivo `.dockerignore` evita copiar arquivos desnecessários para a imagem:

```bash
cat .dockerignore
```

Isso reduz o tamanho da imagem e melhora a segurança.

### 4.3 Construindo a Imagem Docker

```bash
docker build -t mapreduce-app:v1.0 .
```

Aguarde a construção (pode levar alguns minutos na primeira vez).

### 4.4 Verificando a Imagem

```bash
docker images | grep mapreduce-app
```

### ✅ Checkpoint 4.4

Verifique:

- [ ] Você entendeu a estrutura do Dockerfile
- [ ] Build foi concluído sem erros
- [ ] Imagem `mapreduce-app:v1.0` aparece na listagem
- [ ] O tamanho da imagem é razoável (< 200MB)

---

## Parte 5: Executando a Aplicação Containerizada

### 5.1 Executando o Container

Execute o container montando o volume de dados:

**Linux/Mac/Git Bash:**
```bash
docker run --rm \
  -v "$(pwd)/data:/app/data" \
  mapreduce-app:v1.0
```

**Windows PowerShell:**
```powershell
docker run --rm `
  -v "${PWD}/data:/app/data" `
  mapreduce-app:v1.0
```

### 5.2 Testando com Dados Maiores

O script `benchmark.py` já está incluído no repositório. Ele gera automaticamente arquivos de teste de diferentes tamanhos.

Execute o benchmark localmente:

```bash
python3 benchmark.py
```

Isso criará arquivos de teste de 1MB, 5MB e 10MB e medirá o desempenho.

### 5.3 Processando Arquivos Grandes no Container (OPCIONAL)

**Esta seção é opcional.** Se você tiver tempo e interesse, pode explorar o processamento de arquivos maiores.

Execute o processamento de arquivo grande usando argumentos:

**Linux/Mac/Git Bash:**
```bash
docker run --rm \
  -v "$(pwd)/data:/app/data" \
  mapreduce-app:v1.0 \
  python3 mapreduce_runner.py --input data/benchmark_1mb.txt --output data/benchmark_1mb_output.txt
```

**Windows PowerShell:**
```powershell
docker run --rm `
  -v "${PWD}/data:/app/data" `
  mapreduce-app:v1.0 `
  python3 mapreduce_runner.py --input data/benchmark_1mb.txt --output data/benchmark_1mb_output.txt
```


### ✅ Checkpoint 5.3 (OPCIONAL)

Se você realizou esta seção opcional, verifique:

- [ ] Container executou sem erros
- [ ] Benchmark gerou arquivos de teste
- [ ] Você consegue processar arquivos de diferentes tamanhos
- [ ] Entendeu como passar argumentos para o container

---

## Parte 6: Exercícios Práticos

### Exercício 1: Análise Literária - Dom Casmurro (Básico)

O arquivo `data/livro.txt` contém o texto completo do romance "Dom Casmurro" de Machado de Assis, disponível através do Projeto Gutenberg (gutenberg.org). Use MapReduce para analisar:
- As palavras mais frequentes no texto
- Quantas vezes aparecem palavras-chave como "Capitu", "Bentinho", "amor", "ciúme"
- Identificar os termos mais relevantes da obra

**Visualize uma amostra do dataset:**

```bash
head -n 50 data/livro.txt
```

**Tarefa:** Execute o `mapreduce_runner.py` para processar o livro Dom Casmurro.

```bash
python3 mapreduce_runner.py --input data/livro.txt --output data/livro_output.txt
```

**Análise adicional:** Após processar, examine as palavras mais frequentes:

```bash
# Ver as 20 palavras mais frequentes
sort -t$'\t' -k2 -nr data/livro_output.txt | head -20
```

**📸 EVIDÊNCIA OBRIGATÓRIA:**

Após completar o exercício, capture uma evidência da execução:
- Screenshot do terminal mostrando a saída do processamento do livro (incluindo o top 10 de palavras)
- Screenshot do arquivo de saída mostrando as palavras mais frequentes

**Salve esta evidência**, pois você precisará enviá-la na plataforma TEAMS.

### ✅ Checkpoint 6

Complete o exercício:

- [ ] Exercício 1 concluído
- [ ] Evidência capturada e salva

---

## Parte 7: Deployment usando containers via HUB


### 7.1 Publicando no Docker Hub

Publique sua imagem Docker no Docker Hub para compartilhamento:

```bash
# Garanta que não esta logado com nenhuma conta
docker logout

# Login no Docker Hub
docker login

# Tag da imagem com seu usuário do Docker Hub
docker tag mapreduce-app:v1.0 seuusuario/mapreduce-app:v1.0

# Push para o Docker Hub
docker push seuusuario/mapreduce-app:v1.0
```

**Verificando a publicação:**

1. Acesse https://hub.docker.com
2. Faça login com sua conta
3. Verifique que sua imagem aparece nos seus repositórios
4. Compartilhe o link: `docker pull seuusuario/mapreduce-app:v1.0`

### ✅ Checkpoint 7.3

Finalize o projeto:

- [ ] Código commitado no Git
- [ ] Imagem publicada no Docker Hub

---

### ✅ Checkpoint Final

Autoavaliação:

- [ ] Compreendo o paradigma MapReduce profundamente
- [ ] Consigo implementar Map e Reduce para diferentes problemas
- [ ] Sei containerizar aplicações com Docker
- [ ] Entendo os trade-offs de infraestrutura para Big Data
- [ ] Posso explicar o código para outra pessoa
- [ ] Sei publicar imagens Docker no Docker Hub

---

## Parte 8: Entrega da Atividade

### 8.1 O que deve ser entregue

Você deve entregar **evidências** da realização desta atividade prática na plataforma do **Microsoft TEAMS**.

### 8.2 Evidências Obrigatórias

Prepare as seguintes evidências:

1. **Exercício 1 (Análise Literária - Dom Casmurro):**
   - Screenshot da execução do processamento do livro (incluindo estatísticas e top 10)
   - Screenshot do arquivo de saída com as palavras mais frequentes
   - Breve análise: quantas vezes a palavra capitú aparece no livro?

2. **Publicação no Docker Hub:**
   - Screenshot da imagem publicada no Docker Hub
   - Link público para sua imagem (exemplo: `docker pull seuusuario/mapreduce-app:v1.0`)

3. **Link do seu Fork no GitHub:**
   - URL do seu repositório fork com todas as modificações

### 8.3 Como entregar
   - Submeta todas as evidências solicitadas na tarefa que foi atribuida a você na Plataforma Teams.
  
---

## Recursos Adicionais

### Documentação

- [MapReduce Paper (Google)](https://research.google/pubs/pub62/)
- [Docker Documentation](https://docs.docker.com/)
- [Python subprocess module](https://docs.python.org/3/library/subprocess.html)

---


## Conclusão

Parabéns! Você completou a atividade prática de MapReduce com Python e Docker.

### O que você aprendeu

✅ Conceitos fundamentais de MapReduce  
✅ Implementação de pipelines de processamento de dados  
✅ Containerização com Docker  
✅ Boas práticas de infraestrutura para Big Data  
✅ Publicação de imagens no Docker Hub

