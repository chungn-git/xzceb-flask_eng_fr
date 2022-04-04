"""Unit tests translator module
"""

import unittest
from translator import *

class TestTranslateModule(unittest.TestCase):
    def test_null_french_to_english(self):
        self.assertEqual(french_to_english(None), None)
    def test_null_english_to_french(self):
        self.assertIsNone(english_to_french(None), None)
    def test_english_to_french(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour") 
    def test_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

if __name__ == '__main__':
    unittest.main()