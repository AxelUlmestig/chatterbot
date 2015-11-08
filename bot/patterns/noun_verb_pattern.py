import bot.pattern_tools as pt
from knowledge import Noun, Verb

def match_pattern(tree):
	if tree.is_question():
		return None
	verb = pt.find_node(tree, pt.match_POS("VB", "VBD", "VBG", "VBN", "VBP", "VBZ"))
	subject_tree = pt.find_node(verb, pt.match_gram("nsubj"))
	object_tree = pt.find_node(verb, pt.match_gram("dobj"))
	if verb and subject_tree:
		return {"verb_tree": verb, "subject_tree": subject_tree, "object_tree": object_tree}
	return None

def execute_action(knowledge, verb_tree, subject_tree, object_tree):
	noun_subj = Noun(subject_tree)
	noun_obj = None
	if object_tree:
		noun_obj = Noun(object_tree)
	verb = Verb(verb_tree, noun_subj, noun_obj)
	knowledge.add_verb(verb)
	response = "Interesting."
	return response

pattern = pt.create_pattern(execute_action, match_pattern)
