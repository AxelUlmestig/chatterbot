import unittest
from watson import text_to_trees
from knowledge import Knowledge, Noun, Adjective

class KnowledgeTests(unittest.TestCase):

	def test_add_adj_to_noun(self):
		knowledge = Knowledge()
		name = "David"
		info = "cute"
		name_tree = text_to_trees(name)[0]
		info_tree = text_to_trees(info)[0]
		knowledge.add_adj_to_noun(name_tree, info_tree)
		noun = knowledge.get_noun(name_tree)
		description = noun.describe()
		self.assertIn(info, description)

	def test_remove_personal_info(self):
		#Deprecated?
		pass
		#knowledge = Knowledge()
		#name = "David"
		#info = "cute"
		#name_tree = text_to_trees(name)[0]
		#info_tree = text_to_trees(info)[0]
		#knowledge.add_personal_info(name_tree, info_tree)
		#knowledge.remove_personal_info(name_tree, info_tree)
		#name_info = knowledge.get_personal_info(name_tree)
		#self.assertNotIn(info, name_info)

def text_to_obj(text, constructor):
	tree = text_to_trees(text)[0]
	return constructor(tree)

test_class = KnowledgeTests
