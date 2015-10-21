import bot.pattern_tools as pt

def match_pattern(tree):
	if not tree.is_question():
		return None
	adjective = pt.find_node(tree, pt.match_POS("JJ"))
	who = pt.find_node(adjective, pt.match_word("who"))
	if who:
		return {"adjective": adjective}
	return None

def execute_action(knowledge, adjective):
	people = knowledge.get_noun_adj_matches(adjective)
	response = "No one."
	if people:
		response = ""
		for index, person in enumerate(people):
			response += person.word
			if len(people) - index is 1:
				response += "."
			elif len(people) - index is 2:
				response += " and "
			else:
				response += ", " 
	return response

pattern = pt.create_pattern(execute_action, match_pattern)
