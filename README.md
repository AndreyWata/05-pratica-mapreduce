# Atividade Pratica: MapReduce com Python

## Informacoes Gerais

**Publico-alvo:** alunos de graduacao em Ciencia de Dados  
**Tematica:** infraestrutura para projetos de Big Data  
**Nivel:** intermediario  
**Ambiente recomendado:** GitHub Codespaces ou qualquer ambiente Python 3.8+

---

## Objetivos de Aprendizagem

Ao final desta atividade, voce sera capaz de:

1. Explicar os fundamentos do paradigma MapReduce.
2. Implementar as fases Map, Shuffle/Sort e Reduce em Python.
3. Executar um pipeline de processamento de dados em Python puro.
4. Analisar resultados de contagem de palavras em datasets pequenos e maiores.
5. Registrar evidencias tecnicas da execucao da atividade.

---

## Pre-requisitos

- Conhecimento basico de Python.
- Familiaridade com terminal Linux ou Windows.
- Conta no GitHub.

---

## Recursos Necessarios

- **GitHub Codespaces** ou ambiente local com Python 3.8+.
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

## Parte 2: Configuracao do Ambiente

### 2.1 Criando o ambiente no GitHub Codespaces

1. Acesse o repositorio original fornecido pelo professor.
2. Clique em **Fork** para criar uma copia na sua conta.
3. No seu fork, clique em **Code**.
4. Abra a aba **Codespaces**.
5. Clique em **Create codespace on main**.
6. Aguarde o ambiente carregar.

### 2.2 Verificando ferramentas

No terminal, execute:

```bash
python3 --version
```

Voce deve ver a versao do Python instalada (3.8 ou superior).

**EVIDENCIA-01 - Ambiente Python:** capture um print de tela mostrando o comando `python3 --version` e a versao exibida no terminal.

### 2.3 Explorando o projeto

```bash
ls -la
ls -la mapreduce_app
```

No painel lateral do Codespaces, abra o **Explorer** e confira a estrutura completa do projeto. Expanda a pasta `mapreduce_app` e depois a pasta `data`.

Arquivos principais:

- `mapper.py`: implementa a fase Map.
- `reducer.py`: implementa a fase Reduce.
- `mapreduce_runner.py`: orquestra o pipeline completo em Python puro.
- `benchmark.py`: gera datasets de teste e mede desempenho.
- `data/`: contem os datasets usados na atividade.

**EVIDENCIA-02 - Repositorio aberto:** capture um print de tela mostrando o Codespaces com o repositorio aberto e a pasta `mapreduce_app` visivel no Explorer.

### Checkpoint 2

- [ ] O ambiente abriu corretamente.
- [ ] Python esta disponivel (versao 3.8 ou superior).
- [ ] Os arquivos da aplicacao estao visiveis.

---

## Parte 3: Implementacao MapReduce em Python

### 3.1 Entrando no diretorio da aplicacao

```bash
cd mapreduce_app
```

### 3.2 Entendendo o dataset inicial

No Explorer do Codespaces, abra o arquivo `mapreduce_app/data/input.txt` no editor.

Esse arquivo contem frases curtas sobre Big Data e tecnologia. Examine o conteudo diretamente no editor para entender quais palavras deverao aparecer na contagem. Ele sera usado para validar o pipeline antes de processar arquivos maiores.

### 3.3 Analisando o Mapper

No Explorer do Codespaces, abra o arquivo `mapreduce_app/mapper.py` e leia o codigo completo no editor.

O `mapper.py`:

- Le linhas de texto da entrada padrao.
- Converte o texto para minusculas.
- Extrai palavras usando expressao regular.
- Emite pares no formato `palavra<TAB>1`.

Teste isolado do mapper:

```bash
echo "Big data, big systems" | python3 mapper.py
```

Saida esperada:

```text
big     1
data    1
big     1
systems 1
```

### 3.4 Analisando o Reducer

No Explorer do Codespaces, abra o arquivo `mapreduce_app/reducer.py` e leia o codigo completo no editor.

O `reducer.py`:

- Le pares `palavra<TAB>contagem`.
- Soma as contagens por palavra.
- Emite o resultado final ordenado alfabeticamente.

Teste isolado do reducer:

```bash
printf "big\t1\nbig\t1\ndata\t1\n" | python3 reducer.py
```

Saida esperada:

```text
big     2
data    1
```

### 3.5 Entendendo o Runner

No Explorer do Codespaces, abra o arquivo `mapreduce_app/mapreduce_runner.py` e leia o codigo completo no editor.

O `mapreduce_runner.py` executa o pipeline completo em Python puro, sem depender de comandos externos:

```text
arquivo de entrada -> fase Map -> fase Shuffle & Sort (Python) -> fase Reduce -> arquivo de saida
```

Ele tambem exibe estatisticas e as 10 palavras mais frequentes.

### 3.6 Executando o pipeline

```bash
python3 mapreduce_runner.py
```

**EVIDENCIA-03 - Pipeline inicial:** capture um print de tela mostrando a execucao de `python3 mapreduce_runner.py`, incluindo as estatisticas e o top 10 exibidos no terminal.

Depois da execucao, abra o arquivo `mapreduce_app/data/output.txt` pelo Explorer do Codespaces e confira o resultado diretamente no editor.

**EVIDENCIA-04 - Arquivo de saida inicial:** capture um print de tela mostrando o arquivo `data/output.txt` aberto no editor.

### Checkpoint 3

- [ ] O pipeline executou sem erros.
- [ ] O arquivo `data/output.txt` foi criado.
- [ ] As palavras foram contadas corretamente.
- [ ] O terminal exibiu estatisticas e top 10 palavras.

---

## Parte 4: Benchmark de Desempenho

### 4.1 Executando o benchmark

```bash
python3 benchmark.py
```

O script cria arquivos de 1 MB, 5 MB e 10 MB em `data/` e mede o tempo de processamento para cada tamanho.

**EVIDENCIA-05 - Benchmark:** capture um print de tela mostrando a execucao de `python3 benchmark.py` com os tempos registrados no terminal.

### 4.2 Analisando os resultados

O benchmark exibe:

- Tempo de processamento para cada arquivo.
- Throughput em MB/s.

Isso permite visualizar como o modelo MapReduce se comporta conforme o volume de dados cresce.

### 4.3 Processando um arquivo gerado pelo benchmark

Depois de executar o benchmark, processe um arquivo maior diretamente:

```bash
python3 mapreduce_runner.py --input data/benchmark_1mb.txt --output data/benchmark_1mb_output.txt
```

### Checkpoint 4

- [ ] O benchmark gerou arquivos de teste.
- [ ] Os tempos de processamento foram registrados.
- [ ] Um arquivo maior foi processado com sucesso.

---

## Parte 5: Exercicio Pratico - Analise Literaria

O arquivo `data/livro.txt` contem o texto de **Dom Casmurro**, de Machado de Assis, disponibilizado pelo Projeto Gutenberg.

Use MapReduce para analisar:

- Palavras mais frequentes no texto.
- Ocorrencias de termos como `capitú`, `bentinho`, `amor` e `ciume`.
- Termos que aparecem com maior recorrencia na obra.

### 5.1 Visualizando uma amostra

No Explorer do Codespaces, abra o arquivo `mapreduce_app/data/livro.txt` no editor. Use a barra de rolagem ou a busca do editor para observar a estrutura do texto antes do processamento.

### 5.2 Processando o livro

```bash
python3 mapreduce_runner.py --input data/livro.txt --output data/livro_output.txt
```

**EVIDENCIA-06 - Processamento do livro:** capture um print de tela mostrando a execucao do processamento de `data/livro.txt` no terminal.

### 5.3 Analisando as palavras mais frequentes

```bash
sort -t$'\t' -k2 -nr data/livro_output.txt | head -20
```

**EVIDENCIA-07 - Top 20 palavras:** capture um print de tela mostrando o resultado do top 20 de palavras mais frequentes.

### 5.4 Consultando palavras especificas

```bash
grep -E $'^(capitú|bentinho|amor|ciume)\t' data/livro_output.txt
```

> Observacao: o mapper converte palavras para minusculas. Por isso, pesquise por `capitú`, e nao `Capitú`.

**EVIDENCIA-08 - Consulta de termos:** registre em texto quantas vezes a palavra `capitú` aparece no arquivo processado. Se desejar, inclua tambem um print da consulta no terminal.

### Evidencias obrigatorias

Capture evidencias da execucao:

- **EVIDENCIA-06:** screenshot do terminal mostrando o processamento de `data/livro.txt`.
- **EVIDENCIA-07:** screenshot do top 20 de palavras mais frequentes.
- **EVIDENCIA-08:** registro textual informando quantas vezes `capitú` aparece no arquivo processado.

### Checkpoint 5

- [ ] O livro foi processado com sucesso.
- [ ] O arquivo `data/livro_output.txt` foi criado.
- [ ] As palavras mais frequentes foram analisadas.
- [ ] A frequencia de `capitú` foi identificada.
- [ ] As evidencias foram capturadas.

---

## Parte 6: Atividade Extra Opcional - Remocao de Preposicoes e Artigos

Nesta atividade opcional, altere o processamento para remover palavras muito frequentes que nao ajudam tanto na analise, como artigos, preposicoes e conectivos.

Exemplos de palavras que podem ser ignoradas:

```text
o, a, os, as, um, uma, uns, umas, de, da, do, das, dos, em, no, na, nos, nas, por, para, com, e, que
```

### 6.1 Planejando a alteracao

No editor do Codespaces, examine novamente os arquivos `mapper.py`, `reducer.py` e `mapreduce_runner.py`. Decida em qual etapa faz mais sentido eliminar essas palavras.

Sugestao: uma solucao simples e criar uma colecao de palavras ignoradas no `mapper.py` e emitir apenas as palavras que nao estiverem nessa colecao.

### 6.2 Implementando e testando

Depois de modificar o codigo, execute novamente:

```bash
python3 mapreduce_runner.py --input data/livro.txt --output data/livro_sem_stopwords_output.txt
sort -t$'\t' -k2 -nr data/livro_sem_stopwords_output.txt | head -20
```

Compare o novo top 20 com o resultado anterior. Observe se palavras mais relevantes para o conteudo do texto aparecem com mais destaque.

**EVIDENCIA-09 - Extra opcional:** se realizar esta etapa, capture um print de tela mostrando o novo top 20 sem artigos e preposicoes. Inclua tambem uma breve explicacao da estrategia usada.

### Checkpoint Extra Opcional

- [ ] A lista de palavras ignoradas foi definida.
- [ ] O codigo foi alterado sem quebrar o pipeline original.
- [ ] O livro foi processado novamente sem artigos e preposicoes selecionados.
- [ ] O novo resultado foi comparado com o resultado anterior.

---

## Parte 7: Registro no GitHub

Ao final da atividade, registre suas alteracoes no seu fork:

```bash
git status
git add .
git commit -m "conclui atividade mapreduce"
git push
```

Se o Git solicitar configuracao de usuario, execute:

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

1. **Ambiente de desenvolvimento**
   - **EVIDENCIA-01:** screenshot do terminal com `python3 --version`.
   - **EVIDENCIA-02:** screenshot mostrando o repositorio aberto no ambiente.

2. **Processamento MapReduce**
   - **EVIDENCIA-03:** screenshot da execucao de `python3 mapreduce_runner.py`.
   - **EVIDENCIA-04:** screenshot do arquivo `data/output.txt` aberto no editor.

3. **Benchmark**
   - **EVIDENCIA-05:** screenshot da execucao de `python3 benchmark.py` com os tempos registrados.

4. **Analise de Dom Casmurro**
   - **EVIDENCIA-06:** screenshot da execucao com `data/livro.txt`.
   - **EVIDENCIA-07:** screenshot do top 20 de palavras.
   - **EVIDENCIA-08:** resposta textual: quantas vezes a palavra `capitú` aparece?

5. **Atividade extra opcional**
   - **EVIDENCIA-09:** se realizada, screenshot do novo top 20 sem artigos e preposicoes e breve explicacao da estrategia usada.

6. **Repositorio**
   - Link do seu fork no GitHub.

---

## Checkpoint Final

Autoavaliacao:

- [ ] Compreendo o paradigma MapReduce.
- [ ] Consigo explicar Map, Shuffle/Sort e Reduce.
- [ ] Sei executar a aplicacao Python localmente.
- [ ] Consigo interpretar os resultados da contagem de palavras.
- [ ] Tenho evidencias suficientes para entregar a atividade.

---

## Recursos Adicionais

- [MapReduce Paper - Google](https://research.google/pubs/pub62/)
- [GitHub Codespaces Documentation](https://docs.github.com/codespaces)
- [Python subprocess module](https://docs.python.org/3/library/subprocess.html)
- [Python collections module](https://docs.python.org/3/library/collections.html)

---

## Conclusao

Nesta atividade, voce revisou a teoria de MapReduce, implementou e executou um pipeline de contagem de palavras em Python puro, mediu o desempenho com datasets de diferentes tamanhos e analisou um texto literario com o mesmo pipeline.
