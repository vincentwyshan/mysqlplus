#coding=utf8

import ply.yacc as yacc

from mlex import lexer, tokens

start = 'program'

class Statement(object):
    content = None

def p_value(p):
    '''
    value   : STRING
            | INTEGER
            | FLOAT
    '''

def p_setexpression(p):
    '''
    '''


def p_setstatement(p):
    '''
    setstatement : SET VARIABLE EQUAL value
                 | SET VARIABLE EQUAL value DELIMITER'''
    p[0] = p[1]+p[2]+p[3]+p[4]

def p_singlestatement(p):
    '''
    singlestatement : setstatement
    '''
    statement = Statement()
    statement.content = p[1]
    p[0] = statement

def p_compoundstatement(p):
    '''
    compoundstatement : singlestatement singlestatement
    '''
    #p[0] = p[1] + p[2]
    if p[0] == None:
        p[0] = []
    p[0].append(p[1])
    p[0].append(p[2])

def p_statement(p):
    '''
    statement   : compoundstatement
                | singlestatement
    '''
    pass

def p_program(p):
    '''
    program : statement statement
    '''
    pass

def p_error(p):
    print 'Syntax error: %s' % p


def run():
    parser = yacc.yacc()
    s = ''
    while True:
        try:
            s += raw_input('SQL> ')
        except EOFError:
            break
        if not s: continue
        if s.strip().endswith(';'):
            result = parser.parse(s)
            print 'SQL>', 'result:', result 
            s = ''

if __name__ == '__main__':
    run()
