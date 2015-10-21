from watson import call_watson

class SentenceTree:
	def __init__(self, word, POS, grammatical_function, dependency=None):
		self.word = word
		self.POS = POS
		self.grammatical_function = grammatical_function
		self.children = []

	def add_child(self, child):
		self.children.append(child)

	def __str__(self):
		return "({0}, {1}, {2}, {3})".format(self.word, self.POS, self.grammatical_function, self.children)

	def __repr__(self):
		return self.__str__()

	def is_question(self):
		if self.word == "?":
			return True
		for child in self.children:
			if child.is_question():
				return True
		return False

	def is_negated(self):
		for child in self.children:
			if child.grammatical_function == "neg":
				return True
		return False

def _string_to_trees(sentence_string):
	words = sentence_string.split()
	current_node = {}
	trees = []
	for index, word in enumerate(words):
		counter_position = index % 4
		if counter_position is 0:
			current_node = {}
			current_node["word"] = word
		elif counter_position is 1:
			current_node["POS"] = word
		elif counter_position is 2:
			current_node["dependency"] = int(word)
		elif counter_position is 3:
			current_node["grammatical_function"] = word
			st = SentenceTree(**current_node)
			dependency = current_node["dependency"]
			trees.append((st, dependency))
	return trees

def _compile_tree_list(trees):
	root = None
	for pair in trees:
		tree = pair[0]
		dependency = pair[1]
		if tree.grammatical_function == "root":
			root = tree
		if dependency >= 0:
			parent = trees[dependency][0]
			parent.add_child(tree)
	return root

def text_to_trees(text):
	sentences = call_watson(text)
	trees = []
	for sentence in sentences:
		unconnected_trees = _string_to_trees(sentence)
		tree = _compile_tree_list(unconnected_trees)
		trees.append(tree)
	return trees
