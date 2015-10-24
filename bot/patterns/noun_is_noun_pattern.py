import bot.pattern_tools as pt

def match_pattern(tree):
	if tree.is_question():
		return None
	super_noun = pt.find_node(tree, pt.match_POS("NN", "NNS"))
	copular = pt.find_node(super_noun, pt.match_gram("cop"))
	sub_noun = pt.find_child_node(super_noun, pt.match_POS("NN", "NNS", "NNP"))
	if sub_noun and copular:
		return {"super_noun": super_noun, "sub_noun": sub_noun}
	return None

def execute_action(knowledge, super_noun, sub_noun):
	sub_noun_existing = knowledge.get_noun(sub_noun)
	super_noun_existing = knowledge.get_noun(super_noun)
	if sub_noun_existing.add_super_noun(super_noun_existing):
		return "Of course."
	return "That is impossible."
	
pattern = pt.create_pattern(execute_action, match_pattern)
