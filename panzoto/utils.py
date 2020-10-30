from contextlib import contextmanager
import panzoto.config as CFG
import pickle
import functools
import time
import logging

logging.basicConfig(filename='panzoto.log', filemode='w', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


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

def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        logging.info(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer