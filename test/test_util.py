from watson import text_to_trees
from knowledge import Noun, Verb
import unittest
from concurrencytest import ConcurrentTestSuite, fork_for_tests

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

def execute_test_class(test_class):
	loader = unittest.TestLoader()
	suite = unittest.TestSuite()
	suite.addTests(loader.loadTestsFromTestCase(test_class))
	runner = unittest.TextTestRunner()
	concurrent_suite = ConcurrentTestSuite(suite, fork_for_tests(50))
	runner.run(concurrent_suite)
