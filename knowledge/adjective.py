
class Adjective:

	def __init__(self, tree):
		if tree.POS != "JJ":
			raise TypeError("can only create Adjective object from an adjective tree")
		self.word = tree.word
		self.negated = tree.is_negated()
		#self.adverb

	def __str__(self):
		output = self.word
		if self.negated:
			output = "not " + output
		return output
