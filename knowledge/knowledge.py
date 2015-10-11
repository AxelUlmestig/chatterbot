from knowledge.load_initial_knowledge import load_initial_knowledge 

class Knowledge:
	def __init__(self):
		self.proper_nouns = {}
		self.items = self.proper_nouns.items
		load_initial_knowledge(self)

	def add_personal_info(self, name, info):
		name = name.title()
		if name not in self.proper_nouns:
			self.proper_nouns[name] = set()
		person = self.proper_nouns[name]
		person.add(info)

	def get_personal_info(self, name):
		name = name.title()
		if name in self.proper_nouns:
			return self.proper_nouns[name]
		return None

