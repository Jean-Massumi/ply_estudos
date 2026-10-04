# 02 - Lexer: palavras reservadas, linhas e comentários

## Objetivo

Entender como o lexer distingue palavras reservadas de identificadores,
conta linhas e descarta comentários.

## Arquivos

- `lexer.py`: lexer com reservadas, linhas e comentários (modo interativo e modo arquivo)
- `teste.txt`: entrada multilinha para testar a contagem de linhas e comentários
- `exercicio_literals.py`: mesmo lexer usando `literals`

## Como rodar

Modo interativo: digite uma linha por vez (Ctrl+C sai).
Modo arquivo (várias linhas): python lexer.py < teste.txt

## Conceitos

- Dicionário `reservadas` + `t.type = reservadas.get(t.value, 'ID')`
- `t_novalinha` atualiza o lineno
- `t_COMENTARIO` com `pass` descarta o token
- `\#.*`: do # até o fim da linha

## Exercícios

- [x] 1. Testar "se senao senaox" (senaox continua ID)
- [x] 2. Testar "Se" (maiúsculo): vira ID
- [x] 3. Comentar a linha `t.type = ...`: reservadas viram ID
- [x] 4. Remover t_novalinha: lineno fica 1 e o \n cai no t_error
- [x] 5. Adicionar a palavra reservada `imprimir`
- [x] 6. (opcional) Trocar t_MAIS, t_MENOS e t_ATRIBUI por `literals`

## Literals (exercicio_literals.py)

- `literals = ['+', '-', '=']` substitui as variáveis `t_MAIS`, `t_MENOS` e `t_ATRIBUI`.
- Os nomes dos operadores saem da lista `tokens`.
- O tipo do token passa a ser o próprio caractere: `LexToken(+,'+',1,7)`.
- Só serve para 1 caractere. `==` continua precisando de `t_IGUAL`.
- Literais são testados depois das regras normais, então `==` ganha de `=`.
- `t_ignore` não é substituído por `literals`: continua separado.

### Usar ou não

- A favor: menos código, sem regex nem escapes, e na gramática do yacc dá para escrever `'+'`.
- Contra: perde nomes legíveis (`MAIS`), mistura dois estilos quando há operadores compostos, e não aceita lógica.

## Observações

- O dicionário `reservadas` diferencia maiúscula de minúscula: "Se" é ID.
  Para ignorar a diferença, consultar com `t.value.lower()` (decisão de projeto).
- Reservada só vale se o texto for exatamente igual: "senaox" é ID.
- Sem a linha `t.type = reservadas.get(...)`, todas as reservadas viram ID.
- O `\n` não está em t_ignore: sem t_novalinha ele cai no t_error.
- t_novalinha tem dois papéis: consumir o \n e atualizar o lineno.
- Comentário: `\#.*` vai do # até o fim da linha (o `.` não casa \n).
