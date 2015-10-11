import unittest
from bot.bot import Bot

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
		
if __name__ == '__main__':
	unittest.main()

