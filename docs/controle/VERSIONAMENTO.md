> **Referência de modelagem histórica (11/11/2026).** A evidência de execução atual consta do CI e do plano de testes em `docs/PLANO_TESTES.md`; a matriz antiga não implica aprovação.

# Versionamento — Atividade5-EdN

**1.0.0**, 11/11/2026, base `d15f138832354c583ede8d817f56923f4f668b62`. Referências: [projeto](../projeto/ESPECIFICACAO.md), [UML](../uml/README.md), [testes](../testes/PLANO_DE_TESTES.md).

| Versão | Data | Alteração |
|---|---|---|
| 1.0.0 | 11/11/2026 | Inventário dos quatro exercícios, fluxos por fonte e critérios de teste separados |
| 1.0.1 | 26/11/2026 | README e plano de testes registram a ordem de normalização Unicode do palíndromo |

MAJOR para mudança incompatível das assinaturas/saídas; MINOR para novos exercícios; PATCH para ajustes editoriais. Evidências de testes vinculadas ao SHA.

## Revisão de reconciliação — 14/11/2026

Arquivos específicos da antiga modelagem de 11/11 preservados com identificação histórica, sem reverter testes ou código funcional da main. A evidência dos testes aprovados é obtida nas execuções atuais do CI.

## Evidência de 26/11/2026

A regressão falhou antes da correção e passou no SHA `b38a9aada7ad8f142af2548708234c4bc54a2981`. Python 3.11.9 executou `python -m unittest discover -s tests -p 'test_*.py' -v` com 13 testes aprovados e `python -m compileall -q 1 2 3 4 tests` sem erros.
