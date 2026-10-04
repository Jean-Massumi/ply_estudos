import ply.lex as lex

# Palavras reservadas: texto da linguagem -> tipo do token
reservadas = {
    'se': 'SE',
    'senao': 'SENAO',
    'enquanto': 'ENQUANTO',
}

tokens = ['NUMERO', 'ID', 'MAIS', 'MENOS', 'ATRIBUI'] + list(reservadas.values())

t_MAIS = r'\+'
t_MENOS = r'-'
t_ATRIBUI = r'='
t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_COMENTARIO(t):
    r'\#.*'
    pass

def t_novalinha(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caractere inválido: {t.value[0]} na linha {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

entrada = """x = 10
se x
# isto é um comentário
enquanto y
"""

lexer.input(entrada)
for tok in lexer:
    print(tok)
