import unittest
from watson import text_to_trees
from knowledge import Noun, Adjective
from test.test_util import text_to_obj, execute_test_class

class NounTests(unittest.TestCase):
	
	def test_invalid_constructor(self):
		sentence = "very nice"
		tree = text_to_trees(sentence)[0]
		self.assertRaises(TypeError, Noun, tree)

	def test_empty_description(self):
		noun_word = "pig"
		sentence = "a nice " + noun_word
		tree = text_to_trees(sentence)[0]
		noun = Noun(tree)
		expected_description = "I don't know anything about " + noun_word
		description = noun.describe()
		self.assertEqual(expected_description, description)

	def test_description(self):
		noun_word = "pig"
		adj_word1 = "nice"
		adj_word2 = "not cool"
		sentence1 = "the only " + noun_word
		sentence2 = adj_word1
		sentence3 = "very " + adj_word2
		noun_tree = text_to_trees(sentence1)[0]
		adj_tree1 = text_to_trees(sentence2)[0]
		adj_tree2 = text_to_trees(sentence3)[0]
		noun = Noun(noun_tree)
		noun.add_adjective(adj_tree1)
		noun.add_adjective(adj_tree2)
		description = noun.describe()
		self.assertIn(noun_word, description)
		self.assertIn(adj_word1, description)
		self.assertIn(adj_word2, description)

	def test_add_adjective(self):
		noun_str = "pig"
		adj_str1 = "cute"
		adj_str2 = "not " + adj_str1
		noun_tree = text_to_trees(noun_str)[0]
		adj_tree1 = text_to_trees(adj_str1)[0]
		adj_tree2 = text_to_trees(adj_str2)[0]
		noun = Noun(noun_tree)
		adj1 = Adjective(adj_tree1)
		adj2 = Adjective(adj_tree2)
		noun.add_adjective(adj1)
		noun.add_adjective(adj2)
		description = noun.describe()
		self.assertIn(adj_str2, description)

	def test_get_adjective_match1(self):
		adj_str = "sweet"
		noun_str = "pig"
		adj_tree = text_to_trees(adj_str)[0]
		noun_tree = text_to_trees(noun_str)[0]
		adj = Adjective(adj_tree)
		noun = Noun(noun_tree)
		noun.add_adjective(adj)
		adj_match = noun.get_adjective_match(adj)
		self.assertEqual(adj, adj_match)
		
	def test_get_adjective_match2(self):
		adj_str1 = "sweet"
		adj_str2 = "not " + adj_str1
		noun_str = "pig"
		adj_tree1 = text_to_trees(adj_str1)[0]
		adj_tree2 = text_to_trees(adj_str2)[0]
		noun_tree = text_to_trees(noun_str)[0]
		adj1 = Adjective(adj_tree1)
		adj2 = Adjective(adj_tree2)
		noun = Noun(noun_tree)
		noun.add_adjective(adj2)
		adj_match = noun.get_adjective_match(adj1)
		self.assertTrue(adj_match.is_negated)


test_class = NounTests

if __name__ is "__main__":
	execute_test_class(test_class)
