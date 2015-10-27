import unittest
from watson import text_to_trees
from knowledge import Noun, Adjective

class SentenceTreeTests(unittest.TestCase):

	def test_is_negated_true(self):
		text = "not bad"
		tree = text_to_trees(text)[0]
		self.assertTrue(tree.is_negated())

	def test_is_negated_false(self):
		text = "bad"
		tree = text_to_trees(text)[0]
		self.assertFalse(tree.is_negated())

def text_to_obj(text, constructor):
	tree = text_to_trees(text)[0]
	return constructor(tree)

test_class = SentenceTreeTests
