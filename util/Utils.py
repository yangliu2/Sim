from contextlib import contextmanager

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