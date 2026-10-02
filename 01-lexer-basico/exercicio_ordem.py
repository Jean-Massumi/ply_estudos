import ply.lex as lex

tokens = ['IGUAL', 'ATRIBUI']

def t_ATRIBUI(t):
    r'='
    return t

def t_IGUAL(t):
    r'=='
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

entrada = "a == b"

lexer.input(entrada)
for tok in lexer:
    print(tok)