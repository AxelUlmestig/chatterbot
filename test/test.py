import unittest
from concurrencytest import ConcurrentTestSuite, fork_for_tests
from test.load_test_classes import load_test_classes

loader = unittest.TestLoader()
suite = unittest.TestSuite()

for test_class in load_test_classes():
	suite.addTests(loader.loadTestsFromTestCase(test_class))

runner = unittest.TextTestRunner()
concurrent_suite = ConcurrentTestSuite(suite, fork_for_tests(50))
runner.run(concurrent_suite)
