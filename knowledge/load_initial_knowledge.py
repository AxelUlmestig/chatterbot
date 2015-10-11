from os.path import dirname, basename, isfile, realpath
import glob
from importlib import import_module
parent_dir = "knowledge."
if __name__ == "__main__": #debugging
	parent_dir = ""
knowledge_dir = "initial_knowledge"
parent_path = parent_dir + knowledge_dir + "."

path = dirname(realpath(__file__))+"/" + knowledge_dir + "/*.py"
modules = glob.glob(path)

module_names = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith("__init__.py")]
knowledges = [import_module(parent_path + module_name).add_knowledge for module_name in module_names]

if __name__ == "__main__":
	print(knowledges)

def load_initial_knowledge(knowledge):
	for add_knowledge in knowledges:
		add_knowledge(knowledge)
