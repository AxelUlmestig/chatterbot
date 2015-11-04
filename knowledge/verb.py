
class Verb:

	verbs = []

	def __init__(self, tree, subject_noun, object_noun=None):
		if not is_verb_tree(tree):
			raise TypeError("wrong part of speech: " + tree.POS)
		self.word = tree.word
		self.subject_noun = subject_noun
		self.object_noun = object_noun
		Verb.verbs.append(self)

	def __eq__(self, other):
		if not isinstance(other, Verb):
			return False
		if self.word == other.word:
			if self.subject_noun == other.subject_noun:
				return self.object_noun == other.object_noun
		return False

	@staticmethod
	def get_actions(noun):
		actions = []
		for verb in Verb.verbs:
			if verb.subject_noun == noun:
				actions.append(verb)
		return actions
	
	@staticmethod
	def get_acted_on(noun):
		acted_on = []
		for verb in Verb.verbs:
			if verb.object_noun is noun:
				acted_on.append(verb)

	@staticmethod
	def get_verbs(verb):
		verb_matches = []
		for existing_verb in Verb.verbs:
			if existing_verb is verb:
				verb_matches.append(existing_verb)
		return verb_matches


def is_verb_tree(tree):
	if hasattr(tree, "POS"):
		return tree.POS[0:2] == "VB"
	return False
