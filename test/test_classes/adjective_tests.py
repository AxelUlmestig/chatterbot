import unittest
from watson import text_to_trees
from knowledge import Noun, Adjective
from test.test_util import text_to_obj, execute_test_class

class AdjectiveTests(unittest.TestCase):

	def test_constructor(self):
		sentence = "nice"
		tree = text_to_trees(sentence)[0]
		expected_result = sentence
		adj = Adjective(tree)
		self.assertEqual(adj.__str__(), expected_result)

	def test_negation(self):
		sentence = "not nice"
		tree = text_to_trees(sentence)[0]
		expected_result = sentence
		adj = Adjective(tree)
		self.assertEqual(adj.__str__(), expected_result)

	def test_equal_true1(self):
		sentence = "not nice"
		tree1 = text_to_trees(sentence)[0]
		tree2 = text_to_trees(sentence)[0]
		adj1 = Adjective(tree1)
		adj2 = Adjective(tree2)
		self.assertEqual(adj1, adj2)

	def test_equal_true2(self):
		sentence1 = "not nice"
		sentence2 = "nice"
		tree1 = text_to_trees(sentence1)[0]
		tree2 = text_to_trees(sentence2)[0]
		adj1 = Adjective(tree1)
		adj2 = Adjective(tree2)
		self.assertEqual(adj1, adj2)

	def test_not_equal(self):
		sentence1 = "awesome"
		sentence2 = "nice"
		tree1 = text_to_trees(sentence1)[0]
		tree2 = text_to_trees(sentence2)[0]
		adj1 = Adjective(tree1)
		adj2 = Adjective(tree2)
		self.assertNotEqual(adj1, adj2)

	def test_merge_(self):
		sentence1 = "nice"
		sentence2 = "not nice"
		tree1 = text_to_trees(sentence1)[0]
		tree2 = text_to_trees(sentence2)[0]
		adj1 = Adjective(tree1)
		adj2 = Adjective(tree2)
		self.assertFalse(adj1.is_negated)
		self.assertTrue(adj2.is_negated)
		adj1.combine(adj2)
		self.assertTrue(adj1.is_negated)


test_class = AdjectiveTests

if __name__ is "__main__":
	execute_test_class(test_class)
