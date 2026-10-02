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

## Exercícios

- [ ] 1. Trocar a entrada para "x $ 10" e observar o t_error
- [ ] 2. Adicionar \* e / como novos tokens
- [ ] 3. Inverter a ordem de duas regras de função e ver se muda algo

## O que aprendi / dúvidas

(anote aqui)
