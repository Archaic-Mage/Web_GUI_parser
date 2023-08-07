
from bottle import get, post, request, run, static_file
from functools import wraps
from utils import *
import socket
import sys

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
    print("hello")
    return static_file('index.html', root='static')
    
    
@get('/<filename:path>')
def get(filename):
    req_parts = filename.split('/')
    print(req_parts)
    return """<p> done </p>"""
    
@post('/submit')
def submit():
    print('done')
    
def start_server():
    run(host=socket.gethostbyname(socket.gethostname()), port=8080)

def my_fun(*args, **params):
    global html
    global parser_dict
    parser = args[0]
    for name, subparser in iter_parsers(parser):
        print(name)
        for name2, subsubparser in iter_parsers(subparser):
            print(name2)
    start_server()
    return "true"

def wooey(func=None, **gkwargs):
        
    @wraps(func)
    def inner(*args, **kwargs):
        parser_handler = my_fun
        # monkey patch parser
        ArgumentParser.original_parse_args = ArgumentParser.parse_args
        ArgumentParser.parse_args = parser_handler
        # return the wrapped, now monkey-patched, user function
        # to be later invoked
        return func(*args, **kwargs)
        
    return inner  
