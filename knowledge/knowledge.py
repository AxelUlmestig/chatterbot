
class Knowledge:
	def __init__(self):
		self.proper_nouns = {}

	def add_personal_info(self, name, info):
		if name not in self.proper_nouns:
			self.proper_nouns[name] = set()
		person = self.proper_nouns[name]
		person.add(info)

	def get_personal_info(self, name):
		if name in self.proper_nouns:
			return self.proper_nouns[name]
		return None
