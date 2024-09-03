#!/usr/bin/env python3
# import ipdb is a statement that loads the ipdb library in this file when our application runs.
# In the directory of this repo, in your terminal, run the file by typing python lib/ipdb_is_awesome.py
# In the terminal, in your ipdb console, type the variable name inside_the_function and hit enter. You should see a return value of "We're inside the function".
import ipdb

def tracing_the_function():
    inside_the_function = "We're inside the function"
    print(inside_the_function)
    print("We're about to stop because of ipdb!")
    ipdb.set_trace()
    this_variable_hasnt_been_interpreted_yet = \
        "The program froze before it could read me!"
    print(this_variable_hasnt_been_interpreted_yet)

tracing_the_function()
