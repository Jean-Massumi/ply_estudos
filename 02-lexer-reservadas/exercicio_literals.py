import ply.lex as lex

reservadas = {
    'se': 'SE',
    'senao': 'SENAO',
    'enquanto': 'ENQUANTO',
}

tokens = ['NUMERO', 'ID', 'IGUAL'] + list(reservadas.values())

literals = ['+', '-', '=', '*']
t_ignore = ' \t'

t_IGUAL = r'=='

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_novalinha(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caractere inválido: {t.value[0]} na linha {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

# entrada = "x = 10 + y - 2 * a"

# entrada = " a $ b"

entrada = 'a = b == b'

lexer.input(entrada)
for tok in lexer:
    print(tok)