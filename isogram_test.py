import unittest
from isogram import is_isogram

class TestIsogram(unittest.TestCase):

	def test_isogram_with_number(self):
		self.assertFalse(is_isogram("mo0se"))

	def test_isogram_with_text_empty(self):
		self.assertTrue(is_isogram(""))

	def test_is_really_an_isogram(self):
		self.assertTrue(is_isogram("dermatoglyphics"))

	def test_is_not_an_isogram(self):
		self.assertFalse(is_isogram("avocado"))

	def test_is_really_an_isogram_uppercase(self):
		self.assertTrue(is_isogram('Dermatoglyphics'))


if __name__ == '__main__':
    unittest.main()	