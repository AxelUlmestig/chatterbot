from watson import text_to_trees
from knowledge import Noun, Verb

def text_to_obj(text, constructor):
	tree = text_to_trees(text)[0]
	return constructor(tree)

def text_to_verb(text, subj_str, obj_str):
	noun_subj = text_to_obj(subj_str, Noun)
	noun_obj = None
	if obj_str:
		noun_obj = text_to_obj(obj_str, Noun)
	verb_tree = text_to_trees(text)[0]
	return Verb(verb_tree, noun_sbj, noun_obj)
