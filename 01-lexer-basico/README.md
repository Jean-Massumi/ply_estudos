# 01 - Lexer básico

## Objetivo

Entender como o lexer transforma texto em tokens.

## Arquivos

- `lexer.py`: lexer básico (números, `+`, `-`, `*`, `/` e identificadores)
- `exercicio_ordem.py`: exercício 3, ordem das regras (`=` contra `==`)

## Como rodar

python lexer.py

Digite uma entrada por vez no prompt (linha vazia só reabre o prompt;
Ctrl+C sai).

python exercicio_ordem.py

## Saída esperada (entrada: "x + 10 - y")

LexToken(ID,'x',1,0)
LexToken(MAIS,'+',1,2)
LexToken(NUMERO,10,1,4)
LexToken(MENOS,'-',1,7)
LexToken(ID,'y',1,9)

## O que observar

- Os 4 campos de cada token: tipo, valor, linha, posição
- O 10 virou int (por causa do int() em t_NUMERO)
- Erro léxico não vira token: o t_error só imprime a mensagem e o lexer
  continua depois do skip(1)

## Observações

- O lexer pega sempre o trecho mais longo que casa (abc123 vira um ID só).
- ID não pode começar com dígito, mas pode conter dígitos depois.
- "45xyz" vira NUMERO(45) + ID(xyz): o lexer não acusa erro, quem
  rejeitaria isso seria o parser.
- Escape em regex: só em + \* ? . ( ) [ ] { } | ^ $ \ (a / não precisa).
- Nem toda entrada inválida gera erro léxico: "a \*\* b" passa pelo lexer,
  e quem rejeita é o parser.

## Ordem das regras (exercício 3)

- Funções (def t\_...) são testadas na ordem do arquivo; vence a primeira
  que casa, não a mais longa.
- Com t_ATRIBUI (=) antes de t_IGUAL (==), "==" vira dois ATRIBUI.
  Invertendo a ordem, sai um IGUAL só.
- Regra prática: coloque o token mais longo/específico antes do mais curto.
- Variáveis (t_X = r'...') são ordenadas pelo PLY da regex mais longa para
  a mais curta, então a ordem no arquivo não importa para elas.
- Funções sempre são testadas antes das variáveis.
- Use função só quando precisar de lógica (converter valor, contar linhas,
  descartar token) ou de controle de ordem.

## Exercícios

- [x] 1. Trocar a entrada para caractere inválido e observar o t_error
- [x] 2. Adicionar \* e / como novos tokens
- [x] 3. Inverter a ordem de regras de função e comparar (`exercicio_ordem.py`)
