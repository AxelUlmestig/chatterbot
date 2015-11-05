import unittest
from watson import text_to_trees
from knowledge import Knowledge, Noun, Adjective, Verb
from test.test_util import text_to_obj

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
			stored_verb = knowledge.verbs[verb_tree.word]
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
		stored_verb = knowledge.get_verb(verb_tree)
		self.assertEqual(stored_verb, verb)

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


test_class = KnowledgeTests
