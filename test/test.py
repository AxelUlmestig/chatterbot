import unittest
from concurrencytest import ConcurrentTestSuite, fork_for_tests
from bot.bot import Bot
from knowledge import Knowledge
from knowledge import Adjective
from knowledge import Noun
from watson import text_to_trees 

loader = unittest.TestLoader()
suite = unittest.TestSuite()

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

suite.addTests(loader.loadTestsFromTestCase(NounTests))

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

suite.addTests(loader.loadTestsFromTestCase(AdjectiveTests))

class KnowledgeTests(unittest.TestCase):

	def test_add_adj_to_noun(self):
		knowledge = Knowledge()
		name = "David"
		info = "cute"
		name_tree = text_to_trees(name)[0]
		info_tree = text_to_trees(info)[0]
		knowledge.add_adj_to_noun(name_tree, info_tree)
		noun = knowledge.get_noun(name_tree)
		description = noun.describe()
		self.assertIn(info, description)

	def test_remove_personal_info(self):
		#Deprecated?
		pass
		#knowledge = Knowledge()
		#name = "David"
		#info = "cute"
		#name_tree = text_to_trees(name)[0]
		#info_tree = text_to_trees(info)[0]
		#knowledge.add_personal_info(name_tree, info_tree)
		#knowledge.remove_personal_info(name_tree, info_tree)
		#name_info = knowledge.get_personal_info(name_tree)
		#self.assertNotIn(info, name_info)
		
suite.addTests(loader.loadTestsFromTestCase(KnowledgeTests))

class SentenceTreeTests(unittest.TestCase):

	def test_is_negated_true(self):
		text = "not bad"
		tree = text_to_trees(text)[0]
		self.assertTrue(tree.is_negated())

	def test_is_negated_false(self):
		text = "bad"
		tree = text_to_trees(text)[0]
		self.assertFalse(tree.is_negated())

suite.addTests(loader.loadTestsFromTestCase(SentenceTreeTests))

class InitialKnowledgeTests(unittest.TestCase):

	def test_watson_knowledge(self):
		bot = Bot()
		bot_input = "tell me about Watson"
		expected_response = "Watson is the solution to all of humanity's problems."
		response = bot.tell(bot_input)
		#self.assertEqual(response, expected_response)

suite.addTests(loader.loadTestsFromTestCase(InitialKnowledgeTests))

class PatternTests(unittest.TestCase):
	
	def test_random_statement(self):
		bot = Bot()
		bot_input = "asdasdas"
		expected_response = "Ok."
		response = bot.tell(bot_input)
		self.assertEqual(response, expected_response)

	def test_random_question(self):
		bot = Bot()
		bot_input = "asdasdas?"
		expected_response = "I don't know."
		response = bot.tell(bot_input)
		self.assertEqual(response, expected_response)

	def test_greetings(self):
		bot = Bot()
		bot_input = "hello"
		expected_response = bot_input
		response = bot.tell(bot_input)
		self.assertEqual(response, expected_response)

	def test_adj_noun(self):
		bot = Bot()
		bot_input = "David is cute"
		expected_response = "I see."
		response = bot.tell(bot_input)
		self.assertEqual(response, expected_response)

	def test_adj_noun_negated(self):
		bot = Bot()
		bot_input = "David is not cute"
		expected_response = "I see."
		response = bot.tell(bot_input)
		self.assertEqual(response, expected_response)

	def test_adj_removal(self):
		bot = Bot()
		bot_input1 = "David is cute"
		bot_input2 = "David is sweet"
		bot_input3 = "David is not cute"
		bot_input4 = "is David cute?"
		expected_response = "No."
		bot.tell(bot_input1)
		bot.tell(bot_input2)
		bot.tell(bot_input3)
		response = bot.tell(bot_input4)
		self.assertEqual(response, expected_response)

	def test_personal_inquiry1(self):
		bot = Bot()
		bot_input = "who is David?"
		expected_response = "I don't know."
		response = bot.tell(bot_input)
		self.assertEqual(response, expected_response)

	def test_personal_inquiry2(self):
		bot = Bot()
		bot_input = "tell me about David?"
		expected_response = "Who is that?"
		response = bot.tell(bot_input)
		self.assertEqual(response, expected_response)

	def test_personal_inquiry3(self):
		bot = Bot()
		bot_input1 = "David is cute."
		bot_input2 = "who is David?"
		expected_response = bot_input1
		bot.tell(bot_input1)
		response = bot.tell(bot_input2)
		self.assertEqual(response, expected_response)

	def test_personal_inquiry4(self):
		bot = Bot()
		bot_input1 = "David is cute."
		bot_input2 = "tell me about David?"
		expected_response = "David is cute."
		bot.tell(bot_input1)
		response = bot.tell(bot_input2)
		self.assertEqual(response, expected_response)

	def test_adj_inquiry1(self):
		bot = Bot()
		bot_input = "who is cute?"
		expected_response = "No one."
		response = bot.tell(bot_input)
		self.assertEqual(response, expected_response)

	def test_adj_inquiry2(self):
		bot = Bot()
		bot_input1 = "David is cute"
		bot_input2 = "who is cute?"
		expected_response = "David."
		bot.tell(bot_input1)
		response = bot.tell(bot_input2)
		self.assertEqual(response, expected_response)

	def test_adj_inquiry3(self):
		bot = Bot()
		bot_input1 = "David is cute"
		bot_input2 = "Brandon is cute"
		bot_input3 = "who is cute?"
		bot.tell(bot_input1)
		bot.tell(bot_input2)
		response = bot.tell(bot_input3)
		self.assertIn("David", response)
		self.assertIn("Brandon", response)
		
	def test_person_adj_inquiry_true(self):
		bot = Bot()
		bot_input1 = "David is cute"
		bot_input2 = "is David cute?"
		expected_response = "Yes."
		bot.tell(bot_input1)
		response = bot.tell(bot_input2)
		self.assertEqual(response, expected_response)

	def test_person_adj_inquiry_unknown(self):
		bot = Bot()
		bot_input = "is David cute?"
		expected_response = "I don't know who David is."
		response = bot.tell(bot_input)
		self.assertEqual(response, expected_response)

	def test_person_adj_inquiry_false(self):
		bot = Bot()
		bot_input1 = "David is sweet"
		bot_input2 = "is David cute?"
		expected_response = "I don't have that information."
		bot.tell(bot_input1)
		response = bot.tell(bot_input2)
		self.assertEqual(response, expected_response)

suite.addTests(loader.loadTestsFromTestCase(PatternTests))

def text_to_obj(text, constructor):
	tree = text_to_trees(text)[0]
	return constructor(tree)

runner = unittest.TextTestRunner()
concurrent_suite = ConcurrentTestSuite(suite, fork_for_tests(50))
runner.run(concurrent_suite)
