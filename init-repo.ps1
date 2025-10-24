# Script PowerShell para inicializar o repositório Git
# Execute este script para configurar o repositório pela primeira vez

Write-Host "🚀 Inicializando repositório MapReduce Big Data Lab..." -ForegroundColor Green
Write-Host ""

# Verifica se já existe um repositório Git
if (Test-Path ".git") {
    Write-Host "⚠️  Repositório Git já existe!" -ForegroundColor Yellow
    Write-Host "   Para reinicializar, execute: Remove-Item -Recurse -Force .git"
    exit 1
}

# Inicializa o repositório
Write-Host "📦 Inicializando Git..." -ForegroundColor Cyan
git init

# Adiciona todos os arquivos
Write-Host "📝 Adicionando arquivos..." -ForegroundColor Cyan
git add .

# Primeiro commit
Write-Host "💾 Criando commit inicial..." -ForegroundColor Cyan
git commit -m "feat: estrutura inicial do laboratório MapReduce

- Adiciona scripts Python (mapper, reducer, runner, benchmark)
- Adiciona configuração Docker (Dockerfile, compose, dockerignore)
- Adiciona datasets de exemplo (input.txt, logs.txt)
- Adiciona documentação completa (README, roteiro, guias)
- Adiciona .gitignore configurado

Laboratório pronto para clonagem pelos alunos."

Write-Host ""
Write-Host "✅ Repositório inicializado com sucesso!" -ForegroundColor Green
Write-Host ""
Write-Host "📋 Próximos passos:" -ForegroundColor Yellow
Write-Host "   1. Crie um repositório no GitHub"
Write-Host "   2. Execute: git remote add origin https://github.com/SEU_USUARIO/mapreduce-bigdata-lab.git"
Write-Host "   3. Execute: git branch -M main"
Write-Host "   4. Execute: git push -u origin main"
Write-Host "   5. Configure o repositório como template (Settings > Template repository)"
Write-Host ""
Write-Host "📚 Consulte SETUP_REPOSITORIO.md para mais detalhes." -ForegroundColor Cyan
Write-Host ""
