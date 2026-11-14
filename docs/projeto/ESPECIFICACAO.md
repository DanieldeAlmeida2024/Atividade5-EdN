> **Referência de modelagem histórica (11/11/2026).** A evidência de execução atual consta do CI e do plano de testes em `docs/PLANO_TESTES.md`; a matriz antiga não implica aprovação.

# Funções reutilizáveis: gorjeta, palíndromo, desconto e idade

**Documentação v1.0.0**, 11/11/2026 · código auditado `d15f138832354c583ede8d817f56923f4f668b62` · implementação observada estaticamente.

## Escopo real
Quatro scripts independentes de aprendizagem Python, organizados em pastas numeradas. O repositório não contém servidor único nem banco; cada exercício tem seu contrato de entrada/saída e suas dependências próprias. As funções nomeadas abaixo foram encontradas nos arquivos e permitem testes diretos quando isoladas dos blocos de interface.

| Script | Função principal | Implementação e limites |
|---|---|---|
| `1/gorjeta.py` | `calcular_gorjeta` | Gorjeta = conta × porcentagem/100, negativos recusados |
| `2/palindromo.py` | `verificar_palindromo` | lower e regex [^a-z0-9] eliminam pontuação, mas também acentos Unicode |
| `3/desconto.py` | `calcular_preco_com_desconto` | Retorna (valor do desconto, preço final); exige 0≤percentual≤100 |
| `4/idade_em_dias.py` | `calcular_idade_em_dias` | Assume nascimento em 1º de janeiro; usa datetime.date.today |

## Regras de engenharia
O verificador de palíndromo remove letras acentuadas em vez de normalizá-las. O cálculo de idade assume nascimento no primeiro dia do ano, não a data real. As funções existem e podem ser testadas diretamente sem automatizar input().

## Execução
```bash
python 3/desconto.py
python -m unittest discover -s tests -v
```

Não alegar que a suíte de documentação verifica as funções. Identificar as integrações reais e isolar dependências de `input()`, tempo ou HTTP para testes unitários reproduzíveis.
