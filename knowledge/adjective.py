
class Adjective:

	def __init__(self, tree):
		if tree.POS != "JJ":
			raise TypeError("can only create Adjective object from an adjective tree")
		self.word = tree.word.lower()
		self.is_negated = tree.is_negated()
		#self.adverb

	def combine(self, other_adj):
		if self.__eq__(other_adj):
			self.is_negated = other_adj.is_negated
			return True
		return False

	def __str__(self):
		output = self.word
		if self.is_negated:
			output = "not " + output
		return output

	def __eq__(self, other, strict=None):
		if not isinstance(other, Adjective):
			return False
		if self.word == other.word:
			if strict:
				return self.is_negated == other.is_negated
			return True
