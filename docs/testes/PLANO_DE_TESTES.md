> **Referência de modelagem histórica (11/11/2026).** A evidência de execução atual consta do CI e do plano de testes em `docs/PLANO_TESTES.md`; a matriz antiga não implica aprovação.

# Matriz de testes — Atividade5-EdN

**Documentação v1.0.0**, 11/11/2026 · código auditado `d15f138832354c583ede8d817f56923f4f668b62` · implementação observada estaticamente.

| ID | Programa/função | Cenário verificável | Estado |
|---|---|---|---|
| N-T1 | `1/gorjeta.py` / `calcular_gorjeta` | Conta 200, 10% => R$20; conta negativa recusa | Planejado; falta execução |
| N-T2 | `2/palindromo.py` / `verificar_palindromo` | ana = Sim; frase acentuada pode ter normalização errada | Planejado; falta execução |
| N-T3 | `3/desconto.py` / `calcular_preco_com_desconto` | Preço 100, desconto 15% => 15 e 85; 101% recusa | Planejado; falta execução |
| N-T4 | `4/idade_em_dias.py` / `calcular_idade_em_dias` | Ano futuro retorna 0; não calcula idade exata sem mês/dia | Planejado; falta execução |

## Testes de falha
- N01: ausência de entrada, valores vazios ou tipo incompatível.
- N02: limites inferiores/superiores e valores negativos nas funções matemáticas.
- N03: repetir a operação e verificar que não há estado compartilhado inesperado.
- N04: se houver I/O, mockar `requests`, tempo ou aleatoriedade; evitar rede real em CI.

## Evidências
Criar funções de teste `test_*.py` específicas de cada arquivo, usando `unittest.mock` quando pertinente. Registrar Python version, SHA, fixtures, resultado e exceção observada. A suíte existente `tests/test_documentacao.py` não é prova dos cenários de comportamento.
