# EDN05-CLI-03 — EOF e estouro de gorjeta

14/11/2026 · Exercícios gorjeta, palíndromo, desconto e idade aproximada.

## Defeitos
- Os quatro scripts lançavam EOFError sem tratamento quando stdin era encerrado em pipe, terminal ou runner.
- Uma porcentagem e conta individualmente finitas podiam produzir gorjeta ou total infinito, apresentado como `inf`.

## Correções verificáveis
- Todos os CLIs reportam entrada encerrada sem traceback e sem afirmar um resultado inexistente.
- Gorjeta e total são rejeitados quando a aritmética excede o limite finito do float.
- Testes executam cada script sem stdin e cobrem overflow de gorjeta.

## Limites
A estimativa de dias continua a contar desde 1º de janeiro do ano informado, porque dia/mês não foram fornecidos; não é idade exata. Os cálculos financeiros permanecem demonstrações, não sistemas de cobrança contábil.
