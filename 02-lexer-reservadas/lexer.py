import ply.lex as lex
import sys 

# Palavras reservadas: texto da linguagem -> tipo do token
reservadas = {
    'se': 'SE',
    'senao': 'SENAO',
    'enquanto': 'ENQUANTO',
    'imprimir': 'IMPRIMIR'
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

if __name__ == "__main__":
    if sys.stdin.isatty():
        # modo interativo: uma linha por vez
        while True:
            try:
                entrada = input("> ")
            except (EOFError, KeyboardInterrupt):
                break

            if not entrada:
                continue

            lexer.lineno = 1          # reinicia a contagem de linhas
            lexer.input(entrada)
            for tok in lexer:
                print(tok)
    else:
        # modo arquivo: lê tudo de uma vez (aceita várias linhas)
        lexer.lineno = 1
        lexer.input(sys.stdin.read())
        for tok in lexer:
            print(tok)

# Para testar no prompt (uma linha por vez; Ctrl+C sai):
#   se x                -> SE, ID
#   se senao senaox     -> SE, SENAO, ID (senaox não é reservada)
#   Se                  -> ID (o dicionário diferencia maiúscula)
#   x = 10 # comentário -> ID, ATRIBUI, NUMERO (comentário descartado)
#   imprimir x          -> IMPRIMIR, ID
#
# Para testar várias linhas, crie um arquivo (ex.: teste.txt) e rode:
#   python lexer.py < teste.txt
