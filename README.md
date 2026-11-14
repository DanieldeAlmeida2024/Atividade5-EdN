# Atividade5-EdN — atividades Python

Exercícios Python de gorjeta, palíndromo, desconto e idade em dias.

## Execução
Requer Python 3.10+:

```bash
python 1/gorjeta.py
```

**Scripts:** 1/gorjeta.py, 2/palindromo.py, 3/desconto.py, 4/idade_em_dias.py. As atividades são independentes.

## Testes
```bash
python -m unittest discover -s tests -v
```

A suíte acrescentada verifica documentação e sintaxe dos scripts; **não** comprova respostas corretas nem disponibilidade das APIs externas.

## Correções com testes de comportamento

Os quatro exercícios têm verificações automatizadas em Python. A gorjeta e o desconto recusam números negativos, `NaN` e infinito; o palíndromo funciona com acentos e caracteres Unicode e não classifica texto vazio como palíndromo.

O cálculo de **idade em dias a partir de um ano** representa os dias desde **1º de janeiro do ano informado**, considerando anos bissextos. É uma aproximação: para idade real em dias também seriam necessários o dia e o mês de nascimento. Anos futuros são rejeitados.

Execute `python -m unittest discover -s tests -p 'test_*.py' -v`; a suíte é executada pelo GitHub Actions em pull requests e na `main`.

## Atenção
Exercícios didáticos; validar resultados contra os enunciados originais.

Documentos complementares: [requisitos](docs/REQUISITOS.md), [estrutura](docs/ARQUITETURA.md), [UML](docs/UML.puml), [plano de testes](docs/PLANO_TESTES.md), [guia IA](AGENTS.md).

---

## Enunciados originais

### Atividade Prática 05


 1. Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros: valor_conta (float): O valor total da conta porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)
Retorna: float: O valor da gorjeta calculada

 2. Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.

 3. Crie um programa que receba o preço original de um produto e um percentual de desconto, realizando o cálculo do preço final após a aplicação do desconto. Requisitos:

  Permitir que o usuário informe o preço do produto e o percentual de desconto.

  Utilizar operações matemáticas para calcular o valor do desconto e o preço final.

  Exibir o preço final com duas casas decimais para garantir precisão. Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10).


 4. Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.
