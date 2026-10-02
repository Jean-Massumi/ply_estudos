import ply.lex as lex

tokens = ['NUMERO', 'MAIS', 'MENOS', 'ID', 'MULTIPLICA', 'DIVIDE']

t_MAIS = r'\+'
t_MENOS = r'-'
t_MULTIPLICA = r'\*'
t_DIVIDE = r'\/'
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

lexer.input("a * b / 2")
for tok in lexer:
    print(tok)