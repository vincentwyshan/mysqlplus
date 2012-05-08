#coding=utf8

import unittest
import mlex


class LexTest(unittest.TestCase):
    def tokens(self, string):
        mlex.lexer.input(string)
        result = ''
        while True:
            tok = mlex.lexer.token()
            if not tok:
                break
            print tok
            result += tok.value
        return result


    
    def testSimpleSelect(self):
        sql = "SELECT * from mytable"
        self.assertEqual(sql, self.tokens(sql))


    def testComment(self):
        sql = '''
        /* hello world
        haha
        */
        select * from sometable
        '''
        self.assertEqual('select * from sometable', self.tokens(sql).strip())
        sql = '''
        -- comments here
        select * from sometable
        '''
        self.assertEqual('select * from sometable', self.tokens(sql).strip())

    def testMultipleStatement(self):
        sql = '''
        set @a='good';
        select @a, b.* from sometable b;
        '''
        self.assertEqual("set @a='good';        select @a, b.* from sometable b;", self.tokens(sql).strip())


if __name__ == '__main__':
    unittest.main()
