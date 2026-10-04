import ply.lex as lex

tokens = ['NUMERO', 'MAIS', 'MENOS', 'MULTIPLICA', 'DIVIDE',
          'ABRE_PAREN', 'FECHA_PAREN']

t_MAIS = r'\+'
t_MENOS = r'-'
t_MULTIPLICA = r'\*'
t_DIVIDE = r'/'
t_ABRE_PAREN = r'\('
t_FECHA_PAREN = r'\)'
t_ignore = ' \t'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()