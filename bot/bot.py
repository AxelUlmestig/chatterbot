import random
from knowledge import Knowledge
from watson import trees_from_text
from bot.patterns import patterns

class Bot:

	def __init__(self):
		self.knowledge = Knowledge()

	def tell(self, statement):
		trees = trees_from_text(statement)
		questions = [stmt for stmt in trees if stmt.is_question()]
		statements = [stmt for stmt in trees if stmt not in questions]
		if questions:
			return get_answers(questions, self.knowledge, format_question_answers)
		else:
			return get_answers(statements, self.knowledge, format_stmt_answers)


def get_answers(statements, knowledge, format_answers):
	answers = []
	for stmt in statements:
		for match_pattern in patterns:
			answer = match_pattern(stmt, knowledge)
			if answer:
				answers.append(answer)
	return format_answers(answers)

def format_question_answers(answers):
	if not answers:
		return "I don't know"
	output_string = ""
	for answer in answers:
		output_string += answer
	return(output_string)

def format_stmt_answers(answers):
	if not answers:
		return "Ok"
	return random.choice(answers)
