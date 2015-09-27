def create_pattern(execute_action, *match_patterns):
	def match_template(sentence, knowledge):
		for match_pattern in match_patterns:
			key_content = match_pattern(sentence)
			if key_content:
				response = execute_action(knowledge, **key_content)
				return response
		return None
	return match_template

def find_node(tree, criteria):
	if not tree:
		return None
	if criteria(tree):
		return tree
	for child in tree.children:
		descendent_match = find_node(child, criteria)
		if descendent_match:
			return descendent_match
	return None

def match_POS(*POS):
	return create_match_template("POS", *POS)

def match_gram(*grammatical_function):
	return create_match_template("grammatical_function", *grammatical_function)

def match_word(*word):
	return create_match_template("word", *word)

def create_match_template(attribute, *keys):
	def match_template(node):
		for key in keys:
			if getattr(node, attribute).lower() == key.lower():
				return True
		return False
	return match_template
