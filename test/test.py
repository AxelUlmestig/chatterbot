import unittest
from bot.bot import Bot
from watson.sentence_tree import trees_from_text 

class SentenceTreeTests(unittest.TestCase):

	def test_is_negated_true(self):
		text = "not bad"
		tree = trees_from_text(text)[0]
		self.assertTrue(tree.is_negated())

	def test_is_negated_false(self):
		text = "bad"
		tree = trees_from_text(text)[0]
		self.assertFalse(tree.is_negated())

class InitialKnowledgeTests(unittest.TestCase):

	def test_watson_knowledge(self):
		bot = Bot()
		bot_input = "tell me about Watson"
		expected_response = "Watson is the solution to all of humanity's problems."
		response = bot.tell(bot_input)
		self.assertEqual(response, expected_response)

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
		bot_input = "Lorentz is green"
		expected_response = "I see."
		response = bot.tell(bot_input)
		self.assertEqual(response, expected_response)

	def test_personal_inquiry1(self):
		bot = Bot()
		bot_input = "who is Lorentz?"
		expected_response = "I don't know."
		response = bot.tell(bot_input)
		self.assertEqual(response, expected_response)

	def test_personal_inquiry2(self):
		bot = Bot()
		bot_input = "tell me about Lorentz?"
		expected_response = "Who is that?"
		response = bot.tell(bot_input)
		self.assertEqual(response, expected_response)

	def test_personal_inquiry3(self):
		bot = Bot()
		bot_input1 = "Lorentz is cute."
		bot_input2 = "who is Lorentz?"
		expected_response = bot_input1
		bot.tell(bot_input1)
		response = bot.tell(bot_input2)
		self.assertEqual(response, expected_response)

	def test_personal_inquiry4(self):
		bot = Bot()
		bot_input1 = "Lorentz is cute."
		bot_input2 = "tell me about Lorentz?"
		expected_response = "Lorentz is cute."
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
		bot_input1 = "Lorentz is cute"
		bot_input2 = "who is cute?"
		expected_response = "Lorentz."
		bot.tell(bot_input1)
		response = bot.tell(bot_input2)
		self.assertEqual(response, expected_response)

	def test_adj_inquiry3(self):
		bot = Bot()
		bot_input1 = "Lorentz is cute"
		bot_input2 = "Brandon is cute"
		bot_input3 = "who is cute?"
		bot.tell(bot_input1)
		bot.tell(bot_input2)
		response = bot.tell(bot_input3)
		self.assertIn("Lorentz", response)
		self.assertIn("Brandon", response)
		
	def test_person_adj_inquiry_true(self):
		bot = Bot()
		bot_input1 = "Lorentz is cute"
		bot_input2 = "is Lorentz cute?"
		expected_response = "Yes."
		bot.tell(bot_input1)
		response = bot.tell(bot_input2)
		self.assertEqual(response, expected_response)

	def test_person_adj_inquiry_unknown(self):
		bot = Bot()
		bot_input = "is Lorentz cute?"
		expected_response = "I don't know who Lorentz is."
		response = bot.tell(bot_input)
		self.assertEqual(response, expected_response)

	def test_person_adj_inquiry_false(self):
		bot = Bot()
		bot_input1 = "Lorentz is sweet"
		bot_input2 = "is Lorentz cute?"
		expected_response = "Not to my knowledge."
		bot.tell(bot_input1)
		response = bot.tell(bot_input2)
		self.assertEqual(response, expected_response)


if __name__ == '__main__':
	unittest.main()

