from knowledge.load_initial_knowledge import load_initial_knowledge 
from knowledge.noun import Noun
from knowledge.adjective import Adjective
from knowledge.verb import Verb

class Knowledge:
	def __init__(self):
		self.verbs = {}
		self.nouns = {}
		self.noun_relationships = []
		load_initial_knowledge(self)

	def add_noun(self, noun):
		noun_str = noun.word
		if noun_str in self.nouns:
			existing_noun = self.nouns[noun_str]
			existing_noun.combine(noun)
		else:
			self.nouns[noun_str] = noun

	def add_adj_to_noun(self, noun_raw, adjective):
		noun = self.get_noun(noun_raw)
		noun.add_adjective(adjective)

	def get_noun(self, noun_tree):
		noun_str = noun_tree.word
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

	def get_adjective_match(self, noun, adj, strict=None):
		match = noun.get_adjective_match(adj, strict)
		if match:
			return match
		super_nouns = self.get_super_nouns(noun)
		for super_noun in super_nouns:
			super_match = super_noun.get_adjective_match(adj, strict)
			if super_match:
				return super_match
		return None

	def get_super_nouns(self, noun):
		super_relations = [rs for rs in self.noun_relationships if rs.relationship is NounRelationship.SUBSET]
		return [rs.super_noun for rs in super_relations if rs.sub_noun is noun]

	def has_super_noun(self, sub_noun, super_noun):
		super_nouns = self.get_super_nouns(sub_noun)
		if super_noun in super_nouns:
			return True
		for super_noun_old in super_nouns:
			if self.has_super_noun(super_noun_old, super_noun):
				return True
		return False

	def set_super_noun(self, sub_noun, super_noun):
		if sub_noun is super_noun:
			return False
		if self.has_super_noun(sub_noun, super_noun):
			return False
		if self.has_super_noun(super_noun, sub_noun):
			return False
		self.add_noun(sub_noun)
		self.add_noun(super_noun)
		relationship = NounRelationship(sub_noun, super_noun, NounRelationship.SUBSET)
		self.noun_relationships.append(relationship)
		return True

	def add_verb(self, verb):
		if not isinstance(verb, Verb):
			raise TypeError(type(verb) + " is not Verb")
		self.add_noun(verb.get_subject())
		if verb.get_object():
			self.add_noun(verb.get_object())
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

class NounRelationship:
	SUBSET = "subset"

	def __init__(self, sub_noun, super_noun, relationship):
		self.sub_noun = sub_noun
		self.super_noun = super_noun
		self.relationship = relationship

	def matches(sub_noun, super_noun):
		if sub_noun is self.sub_noun:
			return super_noun is self.super_noun
		return False
