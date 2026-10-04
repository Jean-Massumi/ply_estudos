# 03 - Parser: calculadora

## Objetivo

Primeiro contato com o yacc: escrever uma gramática de expressões
aritméticas e calcular o resultado direto nas ações (sem AST ainda).

## Arquivos

- `lexer.py`: tokens NUMERO, MAIS, MENOS, MULTIPLICA, DIVIDE, ABRE_PAREN, FECHA_PAREN
- `parser_calc.py`: gramática e parser (ply.yacc)

## Como rodar

python parser_calc.py

## Gramática

expressao : expressao MAIS expressao
| expressao MENOS expressao
| expressao MULTIPLICA expressao
| expressao DIVIDE expressao
| ABRE_PAREN expressao FECHA_PAREN
| NUMERO

## Conceitos

- GLC: terminais (tokens), não-terminais, produções e símbolo inicial.
- LALR(1): bottom-up, lê da esquerda para a direita, 1 token de lookahead.
- Duas ações: shift (empilha o token) e reduce (troca o lado direito da
  regra pelo esquerdo; é aqui que a função p\_ executa).

## Funções p\_

- A regra fica na docstring; o resultado vai em p[0].
- p[1], p[2]... são os símbolos do lado direito da regra.
- Não executam na ordem do arquivo: executam a cada reduce, de baixo
  para cima na árvore (folhas primeiro).
- A primeira regra do arquivo define o símbolo inicial.
- Em "2 + 3 \* 4": número, número, número, multiplicação, soma.

## precedence

- Só é consultada quando há conflito shift/reduce, na construção da tabela.
- Ordem: da menor para a maior precedência (de cima para baixo).
- Mesma linha = mesma precedência; left/right desempata (10 - 4 - 3 = 3).

## Teste 5: sem precedence

- O PLY avisou 16 conflitos shift/reduce (estados 9 a 12 do parser.out).
- Padrão do PLY em conflito: shift. Resultado: tudo associa à direita
  e sem prioridade entre operadores.
- Exemplos errados sem precedence: "10 - 4 - 3" dá 9, "2 \* 3 + 4" dá 14.
- Estados 8 e 13 e os tokens $end e FECHA_PAREN não têm conflito.

## Entradas de teste

- Válidas: "2 + 3 _ 4" (14), "(2 + 3) _ 4" (20), "10 - 4 - 3" (3)
- Inválidas: "2 +" (fim inesperado), "2 3" (erro sintático, o lexer aceita)
- Observação: com `/`, "10 / 4" dá 2.5 e "8 / 2" dá 4.0 (float); com `//`, dá 2 e 4.

## Exercícios

- [x] 1. "(2 + 3) \* 4"
- [x] 2. "10 - 4 - 3"
- [x] 3. "2 +" e "2 3": erros sintáticos
- [x] 4. Remover a precedence e ler os conflitos no parser.out
- [x] 5. Divisão: decidir se deve ser inteira ou float

## Divisão (exercício 5)

- `/` do Python devolve float, mesmo em divisão exata (8 / 2 = 4.0).
- `//` faz divisão inteira e arredonda para baixo: -7 // 2 = -4 (C daria -3).
- Decisão: usar `//`, porque o lexer só reconhece inteiros.
- No compilador final, seguir a especificação da linguagem do trabalho.
