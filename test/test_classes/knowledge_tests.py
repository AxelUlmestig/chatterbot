import unittest
from watson import text_to_trees
from knowledge import Knowledge, Noun, Adjective, Verb

proper_noun_str1 = "David"
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

	
def text_to_obj(text, constructor):
	tree = text_to_trees(text)[0]
	return constructor(tree)

test_class = KnowledgeTests
