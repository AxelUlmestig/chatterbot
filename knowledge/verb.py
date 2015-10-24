
class Verb:

	verbs = []

	def __init__(self, tree, subject_noun, object_noun=None):
		if not is_verb_tree(tree):
			raise TypeError("wrong part of speech: " + tree.POS)
		self.word = tree.word
		self.subject_noun = subject_noun
		self.object_noun = object_noun
		Verb.verbs.append(self)

	@staticmethod
	def get_actions(noun):
		actions = []
		for verb in Verb.verbs:
			if verb.subject_noun is noun:
				actions.append(verb)
		return actions
	
	@staticmethod
	def get_acted_on(noun):
		acted_on = []
		for verb in Verb.verbs:
			if verb.object_noun is noun:
				acted_on.append(verb)

def is_verb_tree(tree):
	if hasattr(tree, "POS"):
		return tree.POS[0:2] == "VB"
	return False
