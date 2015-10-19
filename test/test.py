import unittest
from concurrencytest import ConcurrentTestSuite, fork_for_tests
from bot.bot import Bot
from knowledge.knowledge import Knowledge
from knowledge.adjective import Adjective
from knowledge.noun import Noun
from watson.sentence_tree import trees_from_text 

loader = unittest.TestLoader()
suite = unittest.TestSuite()

class NounTests(unittest.TestCase):
	
	def test_invalid_constructor(self):
		sentence = "very nice"
		tree = trees_from_text(sentence)[0]
		self.assertRaises(TypeError, Noun, tree)

	def test_empty_description(self):
		noun_word = "pig"
		sentence = "a nice " + noun_word
		tree = trees_from_text(sentence)[0]
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
		noun_tree = trees_from_text(sentence1)[0]
		adj_tree1 = trees_from_text(sentence2)[0]
		adj_tree2 = trees_from_text(sentence3)[0]
		noun = Noun(noun_tree)
		noun.add_adjective(adj_tree1)
		noun.add_adjective(adj_tree2)
		description = noun.describe()
		self.assertIn(noun_word, description)
		self.assertIn(adj_word1, description)
		self.assertIn(adj_word2, description)


suite.addTests(loader.loadTestsFromTestCase(NounTests))

class AdjectiveTests(unittest.TestCase):

	def test_constructor(self):
		sentence = "nice"
		tree = trees_from_text(sentence)[0]
		expected_result = sentence
		adj = Adjective(tree)
		self.assertEqual(adj.__str__(), expected_result)

	def test_negation(self):
		sentence = "not nice"
		tree = trees_from_text(sentence)[0]
		expected_result = sentence
		adj = Adjective(tree)
		self.assertEqual(adj.__str__(), expected_result)

	def test_equal_true1(self):
		sentence = "not nice"
		tree1 = trees_from_text(sentence)[0]
		tree2 = trees_from_text(sentence)[0]
		adj1 = Adjective(tree1)
		adj2 = Adjective(tree2)
		self.assertEqual(adj1, adj2)

	def test_equal_true2(self):
		sentence1 = "not nice"
		sentence2 = "nice"
		tree1 = trees_from_text(sentence1)[0]
		tree2 = trees_from_text(sentence2)[0]
		adj1 = Adjective(tree1)
		adj2 = Adjective(tree2)
		self.assertEqual(adj1, adj2)

	def test_not_equal(self):
		sentence1 = "awesome"
		sentence2 = "nice"
		tree1 = trees_from_text(sentence1)[0]
		tree2 = trees_from_text(sentence2)[0]
		adj1 = Adjective(tree1)
		adj2 = Adjective(tree2)
		self.assertNotEqual(adj1, adj2)

suite.addTests(loader.loadTestsFromTestCase(AdjectiveTests))

class KnowledgeTests(unittest.TestCase):

	def test_add_personal_info(self):
		knowledge = Knowledge()
		name = "David"
		info = "cute"
		knowledge.add_personal_info(name, info)
		name_info = knowledge.get_personal_info(name)
		self.assertIn(info, name_info)

	def test_remove_personal_info(self):
		knowledge = Knowledge()
		name = "David"
		info = "cute"
		knowledge.add_personal_info(name, info)
		knowledge.remove_personal_info(name, info)
		name_info = knowledge.get_personal_info(name)
		self.assertNotIn(info, name_info)
		
suite.addTests(loader.loadTestsFromTestCase(KnowledgeTests))

class SentenceTreeTests(unittest.TestCase):

	def test_is_negated_true(self):
		text = "not bad"
		tree = trees_from_text(text)[0]
		self.assertTrue(tree.is_negated())

	def test_is_negated_false(self):
		text = "bad"
		tree = trees_from_text(text)[0]
		self.assertFalse(tree.is_negated())

suite.addTests(loader.loadTestsFromTestCase(SentenceTreeTests))

class InitialKnowledgeTests(unittest.TestCase):

	def test_watson_knowledge(self):
		bot = Bot()
		bot_input = "tell me about Watson"
		expected_response = "Watson is the solution to all of humanity's problems."
		response = bot.tell(bot_input)
		self.assertEqual(response, expected_response)

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
		expected_response = "Not to my knowledge."
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
		expected_response = "Not to my knowledge."
		bot.tell(bot_input1)
		response = bot.tell(bot_input2)
		self.assertEqual(response, expected_response)

suite.addTests(loader.loadTestsFromTestCase(PatternTests))

runner = unittest.TextTestRunner()
concurrent_suite = ConcurrentTestSuite(suite, fork_for_tests(50))
runner.run(concurrent_suite)
