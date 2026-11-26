# Plano de testes

CT-01 Verificar arquivos e documentação.
CT-02 Analisar sintaxe Python sem executar os scripts.
CT-03 Exercitar casos normais, extremos e inválidos por atividade.
CT-04 Nas atividades externas, simular falha de conexão e resposta inválida.

A suíte `python -m unittest discover -s tests -v` executa CT-01 a CT-03. CT-04 não se aplica aos quatro exercícios locais.

### CT-03 — normalização Unicode no palíndromo

`tests/test_comportamento.py` cobre a equivalência entre maiúsculas e minúsculas com letras matemáticas e sobrescritas, como `𝐀, 𝐚` e `ᴬ a`. `𝐀, 𝐛` continua retornando “Não”. Os casos existentes cobrem acentos, pontuação e texto vazio.
