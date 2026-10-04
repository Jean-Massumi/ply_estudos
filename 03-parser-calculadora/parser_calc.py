import ply.yacc as yacc
from lexer import tokens, lexer

precedence = (
    ('left', 'MAIS', 'MENOS'),
    ('left', 'MULTIPLICA', 'DIVIDE'),
)

def p_expressao_binaria(p):
    '''expressao : expressao MAIS expressao
                 | expressao MENOS expressao
                 | expressao MULTIPLICA expressao
                 | expressao DIVIDE expressao'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] // p[3]

def p_expressao_grupo(p):
    'expressao : ABRE_PAREN expressao FECHA_PAREN'
    p[0] = p[2]

def p_expressao_numero(p):
    'expressao : NUMERO'
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Erro sintático: token inesperado '{p.value}'")
    else:
        print("Erro sintático: fim inesperado da entrada")

parser = yacc.yacc()

if __name__ == "__main__":
    while True:
        try:
            entrada = input("> ")
        
        except (EOFError, KeyboardInterrupt):
            break

        if not entrada:
            continue

        resultado = parser.parse(entrada, lexer=lexer)
        if resultado is not None:
            print(resultado)

# Para testar no terminal (digite uma por vez, linha vazia sai):
#   2 + 3 * 4      -> 14
#   (2 + 3) * 4    -> 20
#   10 - 4 - 3     -> 3
#   5 - 5          -> 0
#   2 +            -> erro sintático
#   10 / 4
#   8 / 2
