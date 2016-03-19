import bot.pattern_tools as pt

def match_pattern(tree):
	if not tree.is_question():
		return None
	verb_tree = pt.find_node(tree, pt.match_POS("VB", "VBD", "VBG", "VBN", "VBP", "VBZ"))
	copular = pt.find_node(verb_tree, pt.match_word("are", "is"))
	subject_tree = pt.find_node(verb_tree, pt.match_gram("nsubj"))
	object_tree = pt.find_node(verb_tree, pt.match_gram("dobj"))
	if copular and verb_tree and subject_tree:
		return {"verb_tree": verb_tree, "subject_tree": subject_tree, "object_tree": object_tree}
	return None

def who_inquiry(knowledge, verb_tree, subject_tree, object_tree):
	negative_response = "No one."
	if object_tree:
		obj = knowledge.get_noun(object_tree)
	matching_verbs = knowledge.get_verbs(verb_tree)
	if object_tree:
		obj = knowledge.get_noun(object_tree)
		matching_verbs = [verb for verb in matching_verbs if verb.get_object() is obj]
	subjs = [verb.get_subject().word for verb in matching_verbs]
	if subjs:
		return format_multiple_answers(subjs)
	return negative_response 

def specific_inquiry(knowledge, verb_tree, subject_tree, object_tree):
	positive_respone = "Yes."
	negative_response = "No."
	subj = knowledge.get_noun(subject_tree)
	obj = None
	if object_tree:
		obj = knowledge.get_noun(object_tree)
	matching_verbs = knowledge.get_verbs(verb_tree)
	matching_subjs = [verb for verb in matching_verbs if verb.get_subject() is subj]
	matches = matching_subjs
	if obj:
		matching_objs = [verb for verb in matching_subjs if verb.get_object() is obj]
		matches = matching_objs
	if len(matches) > 0:
		return positive_respone
	return negative_response

def execute_action(knowledge, verb_tree, subject_tree, object_tree):
	subject_word = subject_tree.word.lower()
	if subject_word == "who":
		return who_inquiry(knowledge, verb_tree, subject_tree, object_tree)
	else:
		return specific_inquiry(knowledge, verb_tree, subject_tree, object_tree)

def format_multiple_answers(answers):
	formatted = ""
	for index, answer in enumerate(answers):
		formatted += answer
		if len(answers) - index is 1:
			formatted += "."
		elif len(answers) - index is 2:
			formatted += " and "
		else:
			formatted += ", "
	return formatted


pattern = pt.create_pattern(execute_action, match_pattern)
