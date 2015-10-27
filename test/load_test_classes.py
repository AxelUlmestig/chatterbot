from os.path import dirname, basename, isfile, realpath
import glob
from importlib import import_module
parent_dir = "test."
test_dir = "test_classes"
parent_path = parent_dir + test_dir + "."

path = dirname(realpath(__file__))+"/" + test_dir + "/*.py"
modules = glob.glob(path)

module_names = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith("__init__.py")]
tests = [import_module(parent_path + module_name).test_class for module_name in module_names]

def load_test_classes():
	return tests
