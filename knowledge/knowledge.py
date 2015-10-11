from knowledge.load_initial_knowledge import load_initial_knowledge 

class Knowledge:
	def __init__(self):
		self.people = {}
		load_initial_knowledge(self)

	def add_personal_info(self, name, info):
		name = name.title()
		if name not in self.people:
			self.people[name] = set()
		person = self.people[name]
		person.add(info)

	def remove_personal_info(self, name, info):
		name = name.title()
		if name not in self.people:
			return
		person = self.people[name]
		if info in person:
			person.remove(info)

	def get_personal_info(self, name):
		name = name.title()
		if name in self.people:
			return self.people[name]
		return None

