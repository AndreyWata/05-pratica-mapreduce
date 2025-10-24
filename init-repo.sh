#!/bin/bash
# Script para inicializar o repositório Git
# Execute este script para configurar o repositório pela primeira vez

echo "🚀 Inicializando repositório MapReduce Big Data Lab..."
echo ""

# Verifica se já existe um repositório Git
if [ -d ".git" ]; then
    echo "⚠️  Repositório Git já existe!"
    echo "   Para reinicializar, execute: rm -rf .git"
    exit 1
fi

# Inicializa o repositório
echo "📦 Inicializando Git..."
git init

# Adiciona todos os arquivos
echo "📝 Adicionando arquivos..."
git add .

# Primeiro commit
echo "💾 Criando commit inicial..."
git commit -m "feat: estrutura inicial do laboratório MapReduce

- Adiciona scripts Python (mapper, reducer, runner, benchmark)
- Adiciona configuração Docker (Dockerfile, compose, dockerignore)
- Adiciona datasets de exemplo (input.txt, logs.txt)
- Adiciona documentação completa (README, roteiro, guias)
- Adiciona .gitignore configurado

Laboratório pronto para clonagem pelos alunos."

echo ""
echo "✅ Repositório inicializado com sucesso!"
echo ""
echo "📋 Próximos passos:"
echo "   1. Crie um repositório no GitHub"
echo "   2. Execute: git remote add origin https://github.com/SEU_USUARIO/mapreduce-bigdata-lab.git"
echo "   3. Execute: git branch -M main"
echo "   4. Execute: git push -u origin main"
echo "   5. Configure o repositório como template (Settings > Template repository)"
echo ""
echo "📚 Consulte SETUP_REPOSITORIO.md para mais detalhes."
echo ""
