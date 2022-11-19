'''
Unit testing translator.py
'''
import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnglishtoFrench(unittest.TestCase):
    '''Testing translation from English to French'''
    def test1(self):
        '''Testing for null input'''
        self.assertIsNone(englishToFrench(None))

    def test2(self):
        '''Testing correctness of input translation for English to French'''
        self.assertEqual(englishToFrench(["Hello"]), ["Bonjour"])


class TestFrenchtoEnglish(unittest.TestCase):
    '''Testing translation from English to French'''
    def test1(self):
        '''
        Testing for null input
        '''
        self.assertIsNone(frenchToEnglish(None))

    def test2(self):
        '''Testing correctness of input translation for French to English'''
        self.assertEqual(frenchToEnglish(["Bonjour"]), ["Hello"])

unittest.main()