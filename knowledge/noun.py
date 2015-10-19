from knowledge.adjective import Adjective
class Noun:

	def __init__(self, noun_tree):
		if not is_noun(noun_tree):
			raise TypeError
		self.word = noun_tree.word
		self.noun_class = noun_tree.POS
		self.adjectives = []

	def add_adjective(self, adjective_tree):
		new_adj = Adjective(adjective_tree)
		for old_adj in self.adjectives:
			if new_adj.combine(old_adj):
				return
		self.adjectives.append(new_adj)

	def describe(self):
		if not self.adjectives:
			return "I don't know anything about " + self.word
		description = self.word + " is "
		for index, adjective in enumerate(self.adjectives):
			description += adjective.__str__()
			if len(self.adjectives) - index is 1:
				description += "."
			elif len(self.adjectives) - index is 2:
				description += " and "
			else:
				description += ", "
		return description

	def combine(self, other_noun):
		if self.__eq__(other_noun):
			#TODO implement
			return True
		return False

	def __eq__(self, other_noun):
		if is_noun(other_noun):
			return other_noun.word == self.word

def is_noun(tree):
	if hasattr(tree, "POS"):
		return tree.POS[0:2] == "NN"
	return false
