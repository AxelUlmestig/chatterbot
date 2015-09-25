from os.path import dirname, basename, isfile, realpath
import glob
from importlib import import_module
parent_dir = "bot."
if __name__ == "__main__": #debugging
	parent_dir = ""
pattern_dir = "patterns_dir"
parent_path = parent_dir + pattern_dir + "."

path = dirname(realpath(__file__))+"/" + pattern_dir + "/*.py"
modules = glob.glob(path)

module_names = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith("__init__.py")]
patterns = [import_module(parent_path + module_name).pattern for module_name in module_names]

if __name__ == "__main__":
	print(patterns)
