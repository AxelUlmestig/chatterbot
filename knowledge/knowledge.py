from knowledge.load_initial_knowledge import load_initial_knowledge 
from knowledge.noun import Noun
from knowledge.adjective import Adjective

class Knowledge:
	def __init__(self):
		self.nouns = {}
		load_initial_knowledge(self)

	def add_adj_to_noun(self, noun_raw, adjective):
		noun = self.get_noun(noun_raw)
		noun.add_adjective(adjective)

	def get_noun(self, noun):
		noun_str = noun.word.lower()
		if noun_str not in self.nouns:
			self.nouns[noun_str] = Noun(noun)
		return self.nouns[noun_str]

	def get_noun_adj_matches(self, adjective, strict=None):
		matches = []
		for noun_str, noun in self.nouns.items():
			current_adj = noun.get_adjective_match(adjective)
			if current_adj:
				if not strict or (adjective.is_negated and current_adj.is_negated):
					matches.append(noun)
		return matches
