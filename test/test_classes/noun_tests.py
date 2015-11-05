import unittest
from watson import text_to_trees
from knowledge import Noun, Adjective
from test.test_util import text_to_obj

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

	def test_add_super_noun_true(self):
		noun_str1 = "pig"
		noun_str2 = "animal"
		sub_noun = text_to_obj(noun_str1, Noun)
		super_noun = text_to_obj(noun_str2, Noun)
		sub_noun.add_super_noun(super_noun)
		super_nouns = sub_noun.get_super_nouns()
		self.assertIn(super_noun, super_nouns)
		
	def test_add_super_noun_false1(self):
		noun_str1 = "pig"
		noun_str2 = "animal"
		sub_noun = text_to_obj(noun_str1, Noun)
		super_noun = text_to_obj(noun_str2, Noun)
		sub_noun.add_super_noun(super_noun)
		super_nouns = super_noun.get_super_nouns()
		self.assertNotIn(sub_noun, super_nouns)

	def test_add_super_noun_false2(self):
		noun_str = "pig"
		noun = text_to_obj(noun_str, Noun)
		self.assertFalse(noun.add_super_noun(noun))

	def test_add_noun_false3(self):
		noun_str1 = "pig"
		noun_str2 = "animal"
		noun_str3 = "lifeform"
		noun1 = text_to_obj(noun_str1, Noun)
		noun2 = text_to_obj(noun_str2, Noun)
		noun3 = text_to_obj(noun_str3, Noun)
		noun1.add_super_noun(noun2)
		noun2.add_super_noun(noun3)
		self.assertFalse(noun3.add_super_noun(noun1), "circular dependency allowed")

	def test_has_super_noun_true1(self):
		noun_str1 = "pig"
		noun_str2 = "animal"
		sub_noun = text_to_obj(noun_str1, Noun)
		super_noun = text_to_obj(noun_str2, Noun)
		sub_noun.add_super_noun(super_noun)
		self.assertTrue(sub_noun.has_super_noun(super_noun))

	def test_has_super_noun_true2(self):
		noun_str1 = "pig"
		noun_str2 = "animal"
		noun_str3 = "lifeform"
		noun1 = text_to_obj(noun_str1, Noun)
		noun2 = text_to_obj(noun_str2, Noun)
		noun3 = text_to_obj(noun_str3, Noun)
		noun1.add_super_noun(noun2)
		noun2.add_super_noun(noun3)
		self.assertTrue(noun1.has_super_noun(noun3))

	def test_has_super_noun_false(self):
		noun_str1 = "pig"
		noun_str2 = "animal"
		sub_noun = text_to_obj(noun_str1, Noun)
		super_noun = text_to_obj(noun_str2, Noun)
		sub_noun.add_super_noun(super_noun)
		self.assertFalse(super_noun.has_super_noun(super_noun))


test_class = NounTests
