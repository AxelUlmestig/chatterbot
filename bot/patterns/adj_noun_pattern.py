import bot.pattern_tools as pt

def match_pattern(tree):
	adjective = pt.find_node(tree, pt.match_POS("JJ"))
	noun = pt.find_node(adjective, pt.match_POS("NNP"))
	if noun and adjective:
		return {"noun": noun.word, "adjective": adjective.word}
	else:
		return None

def execute_action(knowledge, noun, adjective):
	knowledge.add_personal_info(noun, adjective)
	response = "I see."
	return response

pattern = pt.create_pattern(execute_action, match_pattern)

