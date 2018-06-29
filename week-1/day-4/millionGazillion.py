import unittest

class Trie(object):

    def __init__(self):
        self.rootnode={}

    def add_word(self, word):
        presentnode=self.rootnode
        is_new_word=False

        
        for char in word:
            if char not in presentnode:
                is_new_word=True
                presentnode[char]={}
            presentnode=presentnode[char]
            
        if "i" not in presentnode:
            is_new_word=True
            presentnode["i"]={}

        return is_new_word




# Tests

class Test(unittest.TestCase):

    def test_trie_usage(self):
        trie = Trie()

        result = trie.add_word('catch')
        self.assertTrue(result, msg='new word 1')

        result = trie.add_word('cakes')
        self.assertTrue(result, msg='new word 2')

        result = trie.add_word('cake')
        self.assertTrue(result, msg='prefix of existing word')

        result = trie.add_word('cake')
        self.assertFalse(result, msg='word already present')

        result = trie.add_word('caked')
        self.assertTrue(result, msg='new word 3')

        result = trie.add_word('catch')
        self.assertFalse(result, msg='all words still present')

        result = trie.add_word('')
        self.assertTrue(result, msg='empty word')

        result = trie.add_word('')
        self.assertFalse(result, msg='empty word present')


unittest.main(verbosity=2)
