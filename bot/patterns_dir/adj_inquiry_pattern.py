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
	for person, adjectives in knowledge.items():
		for person_adj in adjectives:
			if person_adj.lower() == adjective.lower():
				people.append(person)
	
	if people:
		message = ""
		for index, person in enumerate(people):
			message += person
			if len(people) - index is 1:
				message += "."
			elif len(people) - index is 2:
				message += " and "
			else:
				message += ", " 
		return message
	return "No one"

pattern = pt.create_pattern(execute_action, match_pattern)
