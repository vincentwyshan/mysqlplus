#coding=utf8
'''
Mysql lexer

1. Parse String not Unicode
'''


import re

import ply.lex as lex

keywords = (
        # Or, And, Not, In, Between 
        'OR', 'AND', 'NOT', 'IN', 'BETWEEN',

        # Statemtn Lead word
        'SELECT', 'UPDATE', 'DELETE', 'INSERT',
        'SET', 'EXECUTE', 'PREPARE',
        'CREATE', 'ALTER', 'DROP', 'RENAME', 'TRUNCATE', #DDL
        'CALL', 'SHOW', 
        'DESCRIBE', 'EXPLAIN', 'USE', 'HELP', # Mysql Utility Statement leading
        'BEGIN',
        
        'END', 

        # My plus syntax
        'FOR',
        'IF', 'THEN', 'ELSEIF', 'ELSE', 
        'WHILE', 'DO', 
        'RETURN',

        'WHERE', 'FROM', 'AS', 'INTO', 'INFILE',

        'GLOBAL', 'SESSION',
        
        # 
        #'ADD', 'CHANGE', 'MODIFY', 'PRIMARY', 'KEY',
        #'FIRST', 'AFTER', 'UNIQUE', 'FOREIGN', 'INDEX',
        #'CONSTRAINT', 'COLUMN', 'FULLTEXT', 'DEFAULT',

        )
tokens = (
        # Types 
        'STRING', 'INTEGER', 'FLOAT',
        'VARIABLE',

        # Delimeters ( ) , . 
        'LPAREN', 'RPAREN',
        'COMMA', 'DOT', 
        'DELIMITER',

        # Assignment := = 
        'RETURNASSIGN', #'EQUAL',

        # Operators (+,-,*,/,%,<, <=, >, >=, =, !=, <>)
        'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
        'LT', 'LTE', 'GT', 'GTE', 'EQUAL', 'NOTEQUAL', 'STDNOTEQUAL',

        'BLANK',
        'NAME',
        ) + keywords

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'/\*[\d\D]*?\*/|//.*\n|--.*\n'
    t.lexer.lineno += t.value.count('\n')

def t_STRING(t):
    r"\"([^\"]|\"\"|\\\")*\"|'([^']|''|\\')*'|`(``|[^`])*`" # '', "", ``
    return t

def t_INTEGER(t):
    r'\b[0-9]\d*\b'
    return t

def t_FLOAT(t):
    r'\b\d+\.\d+\b'
    return t

def t_VARIABLE(t):
    r'\@[A-Za-z_][\w_]*|\@\@[A-Za-z_][\w_]*'
    return t

def t_LPAREN(t):
    r'\('
    return t

def t_RPAREN(t):
    r'\)'
    return t

def t_COMMA(t):
    r','
    return t

def t_DOT(t):
    r'\.'
    return t

def t_DELIMITER(t):
    r';'
    return t

def t_RETURNASSIGN(t):
    r'\:\='
    return t

def t_PLUS(t):
    r'\+'
    return t

def t_MINUS(t):
    r'\-'
    return t

def t_DIVIDE(t):
    r'\/'
    return t

def t_TIMES(t):
    r'\*'
    return t

def t_MOD(t):
    r'%'
    return t

def t_LT(t):
    r'\<'
    return t

def t_LTE(t):
    r'\<\='
    return t

def t_GT(t):
    r'\>'
    return t

def t_GTE(t):
    r'\>\='
    return t

def t_EQUAL(t):
    r'\='
    return t

def t_NOTEQUAL(t):
    r'!='
    return t

def t_STDNOTEQUAL(t):
    r'\<\>'
    return t

def t_BLANK(t):
    r'[ \t\x0c]+'
    #return t

#keywords
def t_OR(t):
    'OR'
    return t

def t_AND(t):
    'AND'
    return t

def t_NOT(t):
    'NOT'
    return t

def t_IN(t):
    'IN'
    return t

def t_BETWEEN(t):
    'BETWEEN'
    return t

# Statemtn Lead word
def t_SELECT(t):
    'SELECT'
    return t

def t_UPDATE(t):
    'UPDATE'
    return t

def t_DELETE(t):
    'DELETE'
    return t

def t_INSERT(t):
    'INSERT'
    return t

def t_SET(t):
    r'SET'
    return t

def t_EXECUTE(t):
    'EXECUTE'
    return t

def t_PREPARE(t):
    'PREPARE'
    return t

def t_CREATE(t):
    'CREATE'
    return t

def t_ALTER(t):
    'ALTER'
    return t

def t_DROP(t):
    'DROP'
    return t

def t_RENAME(t):
    'RENAME'
    return t

def t_TRUNCATE(t):
    'TRUNCATE'
    return t

#DDL
def t_CALL(t):
    'CALL'
    return t

# Mysql Utility Statement leading
def t_SHOW(t):
    'SHOW' 
    return t

def t_DESCRIBE(t):
    'DESCRIBE'
    return t

def t_EXPLAIN(t):
    'EXPLAIN'
    return t

def t_USE(t):
    'USE'
    return t

def t_HELP(t):
    'HELP' 
    return t

def t_BEGIN(t):
    'BEGIN'
    return t
        
def t_END(t):
    'END'
    return t

# My plus syntax
def t_FOR(t):
    'FOR'
    return t

def t_IF(t):
    'IF'
    return t

def t_THEN(t):
    'THEN'
    return t

def t_ELSEIF(t):
    'ELSEIF'
    return t

def t_ELSE(t):
    'ELSE'
    return t

def t_WHILE(t):
    'WHILE'
    return t

def t_DO(t):
    'DO'
    return t

def t_RETURN(t):
    'RETURN'
    return t

def t_WHERE(t):
    'WHERE'
    return t
def t_FROM(t):
    'FROM'
    return t
def t_AS(t):
    'AS'
    return t
def t_INTO(t):
    'INTO'
    return t
def t_INFILE(t):
    'INFILE'
    return t


def t_NAME(t):
    r'[A-Za-z_][\w_]*'
    return t

def t_GLOBAL(t):
    r'GLOBAL'
    return t

def t_SESSION(t):
    r'SESSION'
    return t

def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

#for k in MySQLLexer.keywords:
#    setattr(MySQLLexer, 't_%s' % k, k)

#lexer = MySQLLexer()
#lexer.build()
lexer = lex.lex(reflags=re.IGNORECASE)


if __name__ == '__main__':
    s = ''
    while True:
        s += raw_input('> ')
        if s.strip().endswith(';'):
            lexer.input(s)
            s = ''
            while True:
                token = lexer.token()
                if not token:
                    break
                print token
