import bot.pattern_tools as pt

def match_pattern(tree):
	if not tree.is_question():
		return None
	person = pt.find_node(tree, pt.match_POS("NNP"))
	copular = pt.find_node(person, pt.match_gram("cop"))
	adjective = pt.find_node(person, pt.match_POS("JJ"))
	if copular and adjective:
		return {"person": person.word, "adjective": adjective.word}
	return None

def execute_action(knowledge, person, adjective):
	info = knowledge.get_personal_info(person)
	if not info:
		return "I don't know who {0} is.".format(person)
	for existing_adj in info:
		if existing_adj.lower() == adjective.lower():
			return "Yes."
	return "Not to my knowledge."

pattern = pt.create_pattern(execute_action, match_pattern)
