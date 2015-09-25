def create_template(match_pattern, execute_action):
	def match_template(sentence, knowledge):
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

def match_POS(POS):
	def match(node):
		return node.POS == POS
	return match

def match_gram(grammatical_function):
	def match(node):
		return node.grammatical_function == grammatical_function
	return match

def match_word(word):
	def match(node):
		return node.word == word
	return match
