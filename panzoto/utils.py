from contextlib import contextmanager
from pickle import LONG
import panzoto.config as CFG
import pickle
import functools
import time
import logging
from panzoto.enums import Logging, Names
from typing import Callable

logging.basicConfig(
	filename=f'{Names.PANZOTO.value}.log', 
	filemode='a', 
	level=logging.INFO,
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

def log_output(func: Callable):
	"""A decorator that will log the output string returned from a function

	Args:
		func (Callable): function that the decorator is for
	"""
	def wrapper_log(*args, **kwargs):
		output = func(*args, **kwargs)
		log(text=output, 
			level=Logging.INFO.value)
		return output
	return wrapper_log

def log(text: str,
		level: str) -> None:
	"""logging using a central function

	Args:
		text (str): logging text
		level (str): logging level
	"""
	if level == Logging.ERROR.value:
		logging.error(text)
	elif level == Logging.DEBUG.value:
		logging.debug(text)
	elif level == Logging.WARNING.value:
		logging.waring(text)
	else:
		logging.info(text)

	print(text)