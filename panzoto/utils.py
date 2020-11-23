from contextlib import contextmanager
import panzoto.config as CFG
import pickle
import functools
import time
import logging
import pandas as pd
from pathlib import Path
from panzoto.enums import Logging, Names
from typing import Callable

logging.basicConfig(
	filename=f'{CFG.log_dir}/{Names.PANZOTO.value}.log', 
	filemode='a', 
	level=logging.INFO,
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def display_logo():
    logo = """
	         _____    __              ____     ___    _______   ___   
	        /    /   /  |     /|   /     /    /   \      /     /   \  
	       /____/   /___|    / |  /     /    /     \    /     /     \ 
	      /        /    |   /  | /     /     \     /   /      \     / 
	     /        /     |  /   |/     /____   \___/   /        \___/  
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

	if text and CFG.on_screen_print:
		print(text)

def rank_profile(log_path="log/speed.log") -> None:
	"""Sort the cProfile log file to find which process is taking the most
	amount of time.

	Args:
		log_path (str, optional): source log file path. 
		Defaults to "log/speed.log".
	"""

	# skip the first two lines because it's not the correct header
	log_temp = Path(log_path).parent / "temp.log"
	with open(log_path) as input_file, open(log_temp) as output_file:
		next(input_file)
		next(input_file)
		for line in input_file:
			output_file.write(line)

	# use file with correct header to sort columns
	data = pd.read_csv(log_temp,
					   delim_whitespace=True, 
					   error_bad_lines=False)
	sorted = data.sort_values(by=['percall'], ascending=False)
	sorted.to_csv("log/sorted_speed.log", index=False)
