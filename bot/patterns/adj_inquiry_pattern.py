import bot.pattern_tools as pt

def match_pattern(tree):
	if not tree.is_question():
		return None
	adjective = pt.find_node(tree, pt.match_POS("JJ"))
	who = pt.find_node(adjective, pt.match_word("who"))
	if who:
		return {"adjective": adjective.word}
	return None

def execute_action(knowledge, adjective):
	people = []
	for person, adjectives in knowledge.people.items():
		for person_adj in adjectives:
			if person_adj.lower() == adjective.lower():
				people.append(person)
	
	response = "No one."
	if people:
		response = ""
		for index, person in enumerate(people):
			response += person
			if len(people) - index is 1:
				response += "."
			elif len(people) - index is 2:
				response += " and "
			else:
				response += ", " 
	return response

pattern = pt.create_pattern(execute_action, match_pattern)
