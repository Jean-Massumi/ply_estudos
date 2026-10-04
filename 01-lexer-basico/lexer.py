import ply.lex as lex
import sys

tokens = ['NUMERO', 'MAIS', 'MENOS', 'ID', 'MULTIPLICA', 'DIVIDE']

t_MAIS = r'\+'
t_MENOS = r'-'
t_MULTIPLICA = r'\*'
t_DIVIDE = r'/'
t_ID = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_ignore = ' \t'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == "__main__":
    while True:
        try:
            entrada = input("> ")
        except (EOFError, KeyboardInterrupt):
            break

        if not entrada:
            continue

        lexer.input(entrada)
        for tok in lexer:
            print(tok)

# Para testar (digite uma por vez; Ctrl+C sai):
#   x + 10          -> ID, MAIS, NUMERO
#   x & 10          -> ID, aviso de caractere inválido, NUMERO
#   a * b / 2       -> ID, MULTIPLICA, ID, DIVIDE, NUMERO
#   a ** b          -> ID, MULTIPLICA, MULTIPLICA, ID (o lexer aceita)
#   abc123 + x      -> ID, MAIS, ID
#   45xyz           -> NUMERO(45), ID(xyz), sem erro léxico