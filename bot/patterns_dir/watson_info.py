import bot.pattern_tools as pt

def match_pattern(tree):
	if not tree.is_question():
		return None
	watson = pt.find_node(tree, pt.match_word("Watson"))
	if watson:
		return {"watson": watson.word}
	return None

def execute_action(knowledge, watson):
	return "IBM Watson is the solution to all of humanity's problems."

pattern = pt.create_pattern(execute_action, match_pattern)  
