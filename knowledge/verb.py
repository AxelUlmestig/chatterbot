
class Verb:

	def __init__(self, tree, subject_noun, object_noun=None):
		if not is_verb_tree(tree):
			raise TypeError("wrong part of speech: " + tree.POS)
		self.word = tree.word.lower()
		self.subject_noun = subject_noun
		self.object_noun = object_noun

	def get_subject(self):
		return self.subject_noun

	def get_object(self):
		return self.object_noun

	def __eq__(self, other):
		if not isinstance(other, Verb):
			return False
		if self.word == other.word:
			if self.subject_noun == other.subject_noun:
				return self.object_noun == other.object_noun
		return False

def is_verb_tree(tree):
	if hasattr(tree, "POS"):
		return tree.POS[0:2] == "VB"
	return False
