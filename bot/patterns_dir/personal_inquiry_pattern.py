import bot.pattern_tools as pt

def match_pattern1(tree):
	if not tree.is_question():
		return None
	name = pt.find_node(tree, pt.match_POS("NNP"))
	wh_pronoun = pt.find_node(tree, pt.match_POS("WP"))
	if name and wh_pronoun:
		return {"name": name.word}
	return None

def match_pattern2(tree):
	tell = pt.find_node(tree, pt.match_word("tell"))
	person = pt.find_node(tell, pt.match_POS("NNP"))
	about = pt.find_node(person, pt.match_word("about"))
	if about:
		return {"name": person.word}

def execute_action(knowledge, name):
	personal_knowledge = knowledge.get_personal_info(name)
	if personal_knowledge:
		response = name + " is "
		for index, adj in enumerate(personal_knowledge):
			response += adj
			if len(personal_knowledge) - index is 1:
				response += "."
			elif len(personal_knowledge) - index is 2:
				response += " and "
			else:
				response += ", "
		return response
	return None	


pattern = pt.create_pattern(execute_action, match_pattern1, match_pattern2)
