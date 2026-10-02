import ply.lex as lex

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

# Entradas de teste (troque o valor de "entrada"):
#   Ex. 1: "x + 10"        |  "x & 10"
#   Ex. 2: "a * b / 2"     |  "a ** b"
#   Obs.:  "abc123 + x"    |  "45xyz"

entrada = "x + 10"

lexer.input(entrada)
for tok in lexer:
    print(tok)