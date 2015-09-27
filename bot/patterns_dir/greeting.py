import bot.pattern_tools as pt

def match_pattern(tree):
	greeting = pt.find_node(tree, pt.match_word("hi", "hello", "greetings", "howdy"))
	if greeting:
		return {"greeting": greeting.word}
	return None

def execute_action(knowledge, greeting):
	return greeting

pattern = pt.create_template(match_pattern, execute_action)
