# 02 - Lexer: palavras reservadas, linhas e comentários

## Objetivo

Entender como o lexer distingue palavras reservadas de identificadores,
conta linhas e descarta comentários.

## Arquivos

- `lexer.py`: lexer com reservadas (se, senao, enquanto), linhas e comentários

## Como rodar

python lexer.py

## Conceitos

- Dicionário `reservadas` + `t.type = reservadas.get(t.value, 'ID')`
- `t_novalinha` atualiza o lineno
- `t_COMENTARIO` com `pass` descarta o token
- `\#.*`: do # até o fim da linha

## Exercícios

- [ ] 1. Testar "se senao senaox" (senaox deve continuar ID)
- [ ] 2. Testar "Se" (maiúsculo): reservada ou ID? Por quê?
- [ ] 3. Comentar a linha `t.type = ...` e ver o se virar ID
- [ ] 4. Remover o t_novalinha e ver o lineno ficar 1 em tudo
- [ ] 5. Adicionar a palavra reservada `imprimir`
- [ ] 6. (opcional) Trocar t_MAIS, t_MENOS e t_ATRIBUI por `literals`

## Observações

(preencha depois de fazer os exercícios)

## O que aprendi / dúvidas

(anote aqui)
