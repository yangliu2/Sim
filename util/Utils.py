from contextlib import contextmanager
import src.config as CFG
import pickle

def display_logo():
    logo = """
	         _____    __       _        ____     ___    _______   ___   
	        /    /   /  |     / |    /     /    /   \      /     /   \  
	       /____/   /___|    /  |   /     /    /     \    /     /     \ 
	      /        /    |   /   |  /     /     \     /   /      \     / 
	     /        /     |  /    |_/     /____   \___/   /        \___/  
	    ----------------------------------------------------------------
    """
    print(logo)

@contextmanager
def ignored(*exceptions):
	'''ignore exceptions'''

	try:
		yield
	except exceptions:
		pass

def pline(text):
	return text + '\n'

def load_matrix():
	with open(CFG.default_matrix, 'rb') as handle:
		matrix = pickle.load(handle)
	return matrix