import unittest

from translator import frenchToEnglish, englishToFrench

class TestFrenchtoEnglish(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertIsNotNone(frenchToEnglish("Bonjour")) 
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello") 

class TestEnglishtoFrench(unittest.TestCase):
    def test_englishtoFrench(self):
        self.assertIsNotNone(englishToFrench("Hello"))
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

unittest.main()