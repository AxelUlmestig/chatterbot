from knowledge.load_initial_knowledge import load_initial_knowledge 
from knowledge.noun import Noun
from knowledge.adjective import Adjective
from knowledge.verb import Verb

class Knowledge:
	def __init__(self):
		self.verbs = {}
		self.nouns = {}
		load_initial_knowledge(self)

	def add_noun(self, noun):
		noun_str = noun.word.lower()
		if noun_str in self.nouns:
			existing_noun = self.nouns[noun_str]
			existing_noun.combine(noun)
		else:
			self.nouns[noun_str] = noun

	def add_adj_to_noun(self, noun_raw, adjective):
		noun = self.get_noun(noun_raw)
		noun.add_adjective(adjective)

	def get_noun(self, noun_tree):
		noun_str = noun_tree.word.lower()
		if noun_str not in self.nouns:
			self.nouns[noun_str] = Noun(noun_tree)
		return self.nouns[noun_str]

	def get_noun_adj_matches(self, adjective, strict=None):
		matches = []
		for noun_str, noun in self.nouns.items():
			current_adj = noun.get_adjective_match(adjective)
			if current_adj:
				if not strict or (adjective.is_negated and current_adj.is_negated):
					matches.append(noun)
		return matches

	def add_verb(self, verb):
		if not isinstance(verb, Verb):
			raise TypeError(type(verb) + " is not Verb")
		verb_str = verb.word.lower()
		if verb_str not in self.verbs:
			self.verbs[verb_str] = []
		self.verbs[verb.word].append(verb)

	def get_verbs(self, verb_tree = None):
		if verb_tree:
			verb_str = verb_tree.word.lower()
			if verb_str in self.verbs:
				return self.verbs[verb_str]
			return []
		all_verbs = []
		for verb_str in self.verbs:
			all_verbs.extend(self.verbs[verb_str])
		return all_verbs

	def get_actions(self, noun):
		verbs = self.get_verbs()
		return [verb for verb in verbs if verb.get_subject() is noun]

	def get_acted_on(self, noun):
		verbs = self.get_verbs()
		return [verb for verb in verbs if verb.get_object() is noun]
