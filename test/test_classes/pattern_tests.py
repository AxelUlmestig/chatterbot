import unittest
from watson import text_to_trees
from knowledge import Noun, Adjective
from bot import Bot
from test.test_util import text_to_obj, execute_test_class

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
		expected_response = "I don't know anything about David"
		response = bot.tell(bot_input)
		self.assertEqual(response, expected_response)

	def test_personal_inquiry2(self):
		bot = Bot()
		bot_input = "tell me about David?"
		expected_response = "I don't know anything about David"
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
		expected_response = "I don't have that information."
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

	def test_noun_is_noun_true(self):
		bot = Bot()
		bot_input = "David is a pig"
		expected_response = "Of course."
		response = bot.tell(bot_input)
		self.assertEqual(response, expected_response)
		
	def test_noun_is_noun_false(self):
		bot = Bot()
		bot_input1 = "the giraffe is an animal"
		bot_input2 = "the animal is a giraffe"
		expected_response = "That is impossible."
		bot.tell(bot_input1)
		response = bot.tell(bot_input2)
		self.assertEqual(response, expected_response)

	def test_noun_verb(self):
		bot = Bot()
		bot_input = "David is running quickly"
		expected_response = "Interesting."
		response = bot.tell(bot_input)
		self.assertEqual(response, expected_response)

	def test_noun_verb_inquiry_false(self):
		bot = Bot()
		bot_input1 = "David is running quickly"
		bot_input2 = "Is David running?"
		expected_response = "Yes."
		bot.tell(bot_input1)
		response = bot.tell(bot_input2)
		self.assertEqual(response, expected_response)

test_class = PatternTests

if __name__ is "__main__":
	execute_test_class(test_class)
