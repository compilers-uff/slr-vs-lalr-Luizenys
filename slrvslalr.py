import ply.yacc as yacc
import ply.lex as lex

tokens = ('NAME', 'NUMBER', 'TIMES', 'EQUALS')

t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_TIMES   = r'\*'
t_EQUALS  = r'='

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = " \t"

def t_error(t):
    print(f"Illegal character {t.value[0]!r}")
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

lexer = lex.lex()
def p_error(p):
    print("Syntax error in input!")

def p_s(p):
    '''s : l EQUALS r
                    | r'''

def p_l(p):
    '''l : TIMES r
                    | term'''

def p_r(p):
    '''r : l '''

def p_term(p):
    '''term : NAME
                | NUMBER '''

parser = yacc.yacc()
s = "teste"
result = parser.parse(s)
print(result)