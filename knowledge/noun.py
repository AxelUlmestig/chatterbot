from knowledge.adjective import Adjective

class Noun:

	def __init__(self, noun_tree):
		if not is_noun(noun_tree):
			raise TypeError
		self.word = noun_tree.word
		self.noun_class = noun_tree.POS
		self.adjectives = []

	def add_adjective(self, adjective_tree):
		new_adj = format_adj(adjective_tree)
		for old_adj in self.adjectives:
			if old_adj.combine(new_adj):
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
			for adj in other_noun.adjectives:
				self.add_adjective(adj)
			return True
		return False

	def get_adjective_match(self, adjective, strict=None):
		adjective = format_adj(adjective)
		for known_adj in self.adjectives:
			if adjective.__eq__(known_adj, strict):
				return known_adj
		return None

	def __eq__(self, other_noun):
		if isinstance(other_noun, Noun):
			return other_noun.word == self.word
		return False

def is_noun(tree):
	if hasattr(tree, "POS"):
		return tree.POS[0:2] == "NN"
	return False

def format_adj(adj):
	if isinstance(adj, Adjective):
		return adj
	return Adjective(adj)

class NounRelationship:
	
	def __init__(self, sub_noun, super_noun):
		self.sub_noun = sub_noun
		self.super_noun = super_noun

