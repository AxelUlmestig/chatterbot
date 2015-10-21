from knowledge.load_initial_knowledge import load_initial_knowledge 
from knowledge.noun import Noun
from knowledge.adjective import Adjective

class Knowledge:
	def __init__(self):
		self.people = {}
		load_initial_knowledge(self)

	def add_personal_info(self, name, adjective):
		name_str = name.word.lower()
		if name_str not in self.people:
			self.people[name_str] = Noun(name)
		person = self.people[name_str]
		person.add_adjective(adjective)

	def get_personal_info(self, name):
		name_str = name.word.lower()
		if name_str in self.people:
			return self.people[name_str]
		return None

	def get_noun_adj_matches(self, adjective, strict=None):
		matches = []
		for noun_str, noun in self.people.items():
			current_adj = noun.get_adjective_match(adjective)
			if current_adj:
				if not strict or (adjective.is_negated and current_adj.is_negated):
					matches.append(noun)
		return matches
