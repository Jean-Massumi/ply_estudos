# 01 - Lexer básico

## Objetivo

Entender como o lexer transforma texto em tokens.

## Como rodar

python lexer.py

## Saída esperada (entrada: "x + 10 - y")

LexToken(ID,'x',1,0)
LexToken(PLUS,'+',1,2)
LexToken(NUMBER,10,1,4)
LexToken(MINUS,'-',1,7)
LexToken(ID,'y',1,9)

## O que observar

- Os 4 campos de cada token: tipo, valor, linha, posição
- O 10 virou int (por causa do int() em t_NUMBER)

## Observações

- O lexer pega sempre o trecho mais longo que casa (abc123 vira um ID só).
- ID não pode começar com dígito, mas pode conter dígitos depois.
- "45xyz" vira NUMERO(45) + ID(xyz): o lexer não acusa erro, quem
  rejeitaria isso seria o parser.
- Escape em regex: só em + \* ? . ( ) [ ] { } | ^ $ \ (a / não precisa).

## Exercícios

- [x] 1. Trocar a entrada para caractere inválido e observar o t_error
- [x] 2. Adicionar \* e / como novos tokens
- [ ] 3. Inverter a ordem de regras de função e comparar
