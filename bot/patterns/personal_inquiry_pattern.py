import bot.pattern_tools as pt

def match_pattern1(tree):
	if not tree.is_question():
		return None
	name = pt.find_node(tree, pt.match_POS("NNP"))
	wh_pronoun = pt.find_node(tree, pt.match_POS("WP"))
	if name and wh_pronoun:
		return {"name": name, "negative_response": None}
	return None

def match_pattern2(tree):
	tell = pt.find_node(tree, pt.match_word("tell"))
	person = pt.find_node(tell, pt.match_POS("NNP"))
	about = pt.find_node(person, pt.match_word("about"))
	if about:
		return {"name": person, "negative_response": "Who is that?"}

def execute_action(knowledge, name, negative_response):
	person = knowledge.get_noun(name)
	if person:
		return person.describe()
	return negative_response

pattern = pt.create_pattern(execute_action, match_pattern1, match_pattern2)
