import bot.pattern_tools as pt

def match_pattern(tree):
	if not tree.is_question():
		return None
	person = pt.find_node(tree, pt.match_POS("NNP"))
	copular = pt.find_node(person, pt.match_gram("cop"))
	adjective = pt.find_node(person, pt.match_POS("JJ"))
	if copular and adjective:
		return {"person": person, "adjective": adjective}
	return None

def execute_action(knowledge, person, adjective):
	noun = knowledge.get_personal_info(person)
	if not noun:
		return "I don't know who {0} is.".format(person.word)
	adj_match = noun.get_adjective_match(adjective)
	if not adj_match:
		return "I don't have that information."
	if adj_match.is_negated:
		return "No."
	return "Yes."

pattern = pt.create_pattern(execute_action, match_pattern)
