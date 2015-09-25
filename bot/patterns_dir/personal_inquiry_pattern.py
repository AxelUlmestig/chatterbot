import bot.pattern_tools as pt

def match_pattern(tree):
	if not tree.is_question():
		return None
	name = pt.find_node(tree, pt.match_POS("NNP"))
	wh_pronoun = pt.find_node(tree, pt.match_POS("WP"))
	if name and wh_pronoun:
		return {"name": name.word, "wh_pronoun": wh_pronoun.word}
	return None

def execute_action(knowledge, name, wh_pronoun):
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
	return "I don't know. Why don't you tell me?"


pattern = pt.create_template(match_pattern, execute_action)
