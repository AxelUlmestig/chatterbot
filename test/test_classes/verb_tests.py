import unittest
from watson import text_to_trees
from knowledge import Noun, Adjective, Verb
from test.test_util import text_to_obj, text_to_verb

verb_str1 = "running quickly"
verb_str2 = "eating slowly"
noun_str1 = "a sweet crocodile"
noun_str2 = "the smelly goblin"

class VerbTests(unittest.TestCase):

	def test_constructor_fail(self):
		noun_tree = text_to_trees(noun_str1)[0]
		self.assertRaises(TypeError, Verb, noun_tree)

	def test_constructor_pass(self):
		verb_tree = text_to_trees(verb_str1)[0]
		noun = text_to_obj(noun_str1, Noun)
		try:
			verb = Verb(verb_tree, noun)
		except TypeError:
			self.fail("verb constructor threw an exception when given a verb tree")

test_class = VerbTests
