from bottle import get, post, request, run, static_file
from functools import wraps
from utils import *
import socket
from threading import Thread
import os
import signal
import time

## BOTTLE ROUTES (GET / POST) ##

@get('/favicon.ico')
def get_favicon():
    return static_file('favicon.ico', root='static')

@get('/index.js') 
def get_js():
    return static_file('index.js', root='static')

@get('/index.css')
def get_css():
    return static_file('index.css', root='static')

@get('/')
def home():
    return generate_html(parser, '/')
    
@get('/<filename:path>')
def get(filename):
    return generate_html(parser, '/'+filename)
    
@post('/')
def submit():
    set_parsed_args([], request.forms)
    Thread(target=stop_server).start()
    return """<p> done </p>"""

@post('/<filename:path>')
def submit(filename):
    args = filename.split('/')
    set_parsed_args(args, request.forms)
    Thread(target=stop_server).start()
    return """<p> done </p>"""


## Helper functions ##

def stop_server():
    """!
    stops the bottle server by sending a signal Interrupt.
    Similar to Ctrl - C (signal)
    """
    print('Stopping Server...')
    time.sleep(1)
    pid = os.getpid()
    os.kill(pid, signal.SIGINT)
    
def start_server():
    run(host=socket.gethostbyname(socket.gethostname()), port=8080)
    
def set_parsed_args(args, form_data):
    """!
    Parses the response received by the form and set the parsed data
    according to the parsing method specified by user in the original parse_ars() function
    """
    global parsed_args
    args.extend(parse_gui_args(form_data))
    args = parser.original_parse_args(args)
    parsed_args = args

## WOOEY DECORATOR ##

def wooey_wrap(*args, **params):
    """!
    Patched function to parsing argument
    - starts the server (bottle)
    - generates form data and sets parsed data
    - returns the parsed data
    """
    global parser
    parser = args[0]
    start_server()
    return parsed_args

def wooey(func=None, **gkwargs):
    """
    Patching the default argument parsing function to
    custom made wooey wrapper (Uses Monkey Patching)
    """        
    @wraps(func)
    def inner(*args, **kwargs):
        parser_handler = wooey_wrap
        # monkey patch parser
        ArgumentParser.original_parse_args = ArgumentParser.parse_args
        ArgumentParser.parse_args = parser_handler
        # return the wrapped, now monkey-patched, user function
        # to be later invoked
        return func(*args, **kwargs)
        
    return inner  
