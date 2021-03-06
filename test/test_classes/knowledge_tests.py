import unittest
from watson import text_to_trees
from knowledge import Knowledge, Noun, Adjective, Verb
from test.test_util import text_to_obj, execute_test_class

proper_noun_str1 = "David"
proper_noun_str2 = "Alice"
adjective_str1 = "cute"
verb_str1 = "eating a banana"

class KnowledgeTests(unittest.TestCase):

	def test_add_adj_to_noun(self):
		knowledge = Knowledge()
		name_tree = text_to_trees(proper_noun_str1)[0]
		info_tree = text_to_trees(adjective_str1)[0]
		knowledge.add_adj_to_noun(name_tree, info_tree)
		noun = knowledge.get_noun(name_tree)
		description = noun.describe()
		self.assertIn(adjective_str1, description)

	def test_get_noun_false(self):
		knowledge = Knowledge()
		name_tree = text_to_trees(proper_noun_str1)[0]
		noun_in_knowledge = knowledge.get_noun(name_tree)
		self.assertEquals(noun_in_knowledge.word, proper_noun_str1)

	def test_add_verb(self):
		knowledge = Knowledge()
		verb_tree = text_to_trees(verb_str1)[0]
		noun_tree = text_to_trees(proper_noun_str1)[0]
		noun = text_to_obj(noun_tree, Noun)
		verb = Verb(verb_tree, noun)
		knowledge.add_verb(verb)
		try:
			stored_verb = knowledge.verbs[verb_tree.word][0]
			self.assertEqual(stored_verb, verb)
		except:
			self.fail("verb not added to knowledge verb dict")

	def test_get_verb(self):
		knowledge = Knowledge()
		verb_tree = text_to_trees(verb_str1)[0]
		noun_tree = text_to_trees(proper_noun_str1)[0]
		noun = text_to_obj(noun_tree, Noun)
		verb = Verb(verb_tree, noun)
		knowledge.add_verb(verb)
		stored_verb_matches = knowledge.get_verbs(verb_tree)
		self.assertIn(verb, stored_verb_matches)

	def test_get_actions_true(self):
		knowledge = Knowledge()
		verb_tree = text_to_trees(verb_str1)[0]
		noun_tree = text_to_trees(proper_noun_str1)[0]
		noun = text_to_obj(noun_tree, Noun)
		verb = Verb(verb_tree, noun)
		knowledge.add_verb(verb)
		action = knowledge.get_actions(noun)[0]
		self.assertEqual(action, verb)

	def test_get_actions_false(self):
		knowledge = Knowledge()
		verb_tree = text_to_trees(verb_str1)[0]
		noun_tree = text_to_trees(proper_noun_str1)[0]
		noun_tree_other = text_to_trees(proper_noun_str2)[0]
		noun = text_to_obj(noun_tree, Noun)
		noun_other = text_to_obj(noun_tree_other, Noun)
		verb = Verb(verb_tree, noun)
		knowledge.add_verb(verb)
		actions = knowledge.get_actions(noun_other)
		nbr_of_actions = len(actions)
		expected_actions = 0
		self.assertEqual(nbr_of_actions, expected_actions)

	def test_get_acted_on_true(self):
		knowledge = Knowledge()
		verb_tree = text_to_trees(verb_str1)[0]
		noun_tree_subject = text_to_trees(proper_noun_str1)[0]
		noun_tree_object = text_to_trees(proper_noun_str2)[0]
		noun_subject = text_to_obj(noun_tree_subject, Noun)
		noun_object = text_to_obj(noun_tree_object, Noun)
		verb = Verb(verb_tree, noun_subject, noun_object)
		knowledge.add_verb(verb)
		acted_on = knowledge.get_acted_on(noun_object)[0]
		self.assertEqual(acted_on, verb)

	def test_get_acted_on_false(self):
		knowledge = Knowledge()
		verb_tree = text_to_trees(verb_str1)[0]
		noun_tree_subject = text_to_trees(proper_noun_str1)[0]
		noun_tree_object = text_to_trees(proper_noun_str2)[0]
		noun_subject = text_to_obj(noun_tree_subject, Noun)
		noun_object = text_to_obj(noun_tree_object, Noun)
		verb = Verb(verb_tree, noun_subject, noun_object)
		knowledge.add_verb(verb)
		acted_on_list = knowledge.get_acted_on(noun_subject)
		nbr_of_acted_on = len(acted_on_list)
		expected_acted_on = 0
		self.assertEqual(nbr_of_acted_on, expected_acted_on)

	def test_add_super_noun_true(self):
		knowledge = Knowledge()
		noun_str1 = "pig"
		noun_str2 = "animal"
		sub_noun = text_to_obj(noun_str1, Noun)
		super_noun = text_to_obj(noun_str2, Noun)
		knowledge.set_super_noun(sub_noun, super_noun)
		super_nouns = knowledge.get_super_nouns(sub_noun)
		self.assertIn(super_noun, super_nouns)
		
	def test_add_super_noun_false1(self):
		knowledge = Knowledge()
		noun_str1 = "pig"
		noun_str2 = "animal"
		sub_noun = text_to_obj(noun_str1, Noun)
		super_noun = text_to_obj(noun_str2, Noun)
		knowledge.set_super_noun(sub_noun, super_noun)
		super_nouns = knowledge.get_super_nouns(super_noun)
		self.assertNotIn(sub_noun, super_nouns)

	def test_add_super_noun_false2(self):
		knowledge = Knowledge()
		noun_str = "pig"
		noun = text_to_obj(noun_str, Noun)
		self.assertFalse(knowledge.set_super_noun(noun, noun))

	def test_add_noun_false3(self):
		knowledge = Knowledge()
		noun_str1 = "pig"
		noun_str2 = "animal"
		noun_str3 = "lifeform"
		noun1 = text_to_obj(noun_str1, Noun)
		noun2 = text_to_obj(noun_str2, Noun)
		noun3 = text_to_obj(noun_str3, Noun)
		knowledge.set_super_noun(noun1, noun2)
		knowledge.set_super_noun(noun2, noun3)
		self.assertFalse(knowledge.set_super_noun(noun3, noun1))

	def test_has_super_noun_true1(self):
		knowledge = Knowledge()
		noun_str1 = "pig"
		noun_str2 = "animal"
		sub_noun = text_to_obj(noun_str1, Noun)
		super_noun = text_to_obj(noun_str2, Noun)
		knowledge.set_super_noun(sub_noun, super_noun)
		self.assertTrue(knowledge.has_super_noun(sub_noun, super_noun))

	def test_has_super_noun_true2(self):
		knowledge = Knowledge()
		noun_str1 = "pig"
		noun_str2 = "animal"
		noun_str3 = "lifeform"
		noun1 = text_to_obj(noun_str1, Noun)
		noun2 = text_to_obj(noun_str2, Noun)
		noun3 = text_to_obj(noun_str3, Noun)
		knowledge.set_super_noun(noun1, noun2)
		knowledge.set_super_noun(noun2, noun3)
		self.assertTrue(knowledge.has_super_noun(noun1, noun3))

	def test_has_super_noun_false(self):
		knowledge = Knowledge()
		noun_str1 = "pig"
		noun_str2 = "animal"
		sub_noun = text_to_obj(noun_str1, Noun)
		super_noun = text_to_obj(noun_str2, Noun)
		knowledge.set_super_noun(sub_noun, super_noun)
		self.assertFalse(knowledge.has_super_noun(super_noun, super_noun))





test_class = KnowledgeTests

if __name__ is "__main__":
	execute_test_class(test_class)
