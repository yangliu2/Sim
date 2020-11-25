# Panzoto
Pet project for human simulation

Run `python main.py` to start the interaction in prompt

# tests
`bash test.sh` to run the tests.   
Some functions are probablistic, and may fail at a small chance.  

# to run 
`python main.py` to run the main portal. 

# generate cProfile graphs
`bash graph_usage.sh`  

# structure
`data/` include all the saved data as a pickle file  
`data/graphs/` are where graphs goes  
`log/` include logging, cProfile files and graphs  
`panzoto/` are the source code  
`tests/` have the unit tests   
`htmlcov/` coverage generated unittest coverage map  

# use coverage to check unit test coverage  
`coverage run -m unittest discover tests` to generaet .coverage file
`coverage report -m` to generate a report in cli  
`coverage html` to generate the `htmlcov/` folder with interactive map  

# List of Commands
**create_person**  
`create_person <first name> <last name>`  
Create a person based on first and last name. Stats are randomly generated

**create_child**  
`create_child`  
Create a child. It will randomly search for a female and a male in the current population. Stats are randomly generated with full health just like a new person. 

**remove_person**  
`remove_person <uid>`  
Delete a person from the population using unique uid. Can use `focus` to find the uid. Need to convert the uid string into UUID object.

**list_people**  
`list_people`  
List all the people who are present in the current population.  

**create_food**  
`create_food <name> <value>`  
Create a food item for the people to consume. 

**remove_item**  
`remove_item <uid>`  
Remove an item using the uid. Use `focus <item name>` to find the uid. 

**assign**  
`assign <item uid> <person uid>`    
Assign an item to a person by item and person uid. 

**list_items**  
`list_items`  
List all the items that exists. 

**run_turns**  
`run_turns <number of turns>`  
Run the simulation for n number of turns. Checks are done for each person and item at the end of each turn.

**focus**  
`focus <first name> <last name>`  
Focus on a specific person for stats.  
`focus <item name>`  
Focus on a specific item for stats. 

**display_stats**  
`display_stats`  
Show population level stats.  

**help**  
`help`  
Use this to generate a list of commands in a dictionary. 

**exit**  
`exit`, `quit`, `bye`  
This is a current list of commands that will quit the program
