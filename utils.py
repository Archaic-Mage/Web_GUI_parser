"""!
@brief Utility functions for the project.

This contains fucntions for loading the parsing parameters and generating the corresponding HTML forms.
"""

from js import JS
from html import HEAD
from argparse import (ArgumentParser, _SubParsersAction)

def generate_div(input_type, placeholder, metavar, multiple=False):

    if multiple:
        string = f'''
            <input class="text-holder" type=text id="{input_type}-0" name="{input_type}-0">
            <input class="add-btn" name="{input_type}-0" type="button" value="+" onclick="add_input_field(this)">
            '''
    else :
        string = f'''<input class="text-holder" type=text id="{input_type}" name="{input_type}">'''

    return f"""<div>
    <label class="input-type" for="{input_type}">{metavar}</label><br>
    <label class="placeholder">{placeholder}</label><br>
    {string}
</div>
"""

def generate_form(parser):
    request_type = parser.prog.split()[1]
    actions = parser._optionals._actions
    form = f"""<form action="/" method="post">\n"""
    for i in range(1, len(actions)):
        metavar = actions[i].metavar
        placeholder = actions[i].help
        input_type = actions[i].dest
        if actions[i].nargs == '*':
            form += generate_div(input_type, placeholder, metavar, multiple=True)
        else:
            form += generate_div(input_type, placeholder, metavar)
    form += f"""<input class="button" type="submit" value="Submit">\n"""
    form += f"""</form>"""
    return form

def generate_html(subparser):
    HTML = "<html>\n" + HEAD + "<body>\n" + generate_form(subparser) + "</body>\n" + JS + "</html>"
    return HTML


# for parsing the reponse from the form
# WEB GUI FUNCTIONS
def parse_gui_args(gui_dict):

    args = []
    args_dict = {}

    for key in gui_dict.keys():
        if len(gui_dict[key].strip())==0:
            continue
        arg = key.split('-')[0]
        if arg not in args_dict:
            args_dict[arg] = []
        args_dict[arg].append(gui_dict[key])

    for key in args_dict.keys():
        args.append(f"--{key}")
        args.extend(args_dict[key])

    return args

def is_subparser(action):
    return isinstance(action, _SubParsersAction)

def get_subparser(actions):
    return list(filter(is_subparser, actions))[0]

def iter_parsers(parser):
    ''' Iterate over name, parser pairs '''
    try:
        return get_subparser(parser._actions).choices.items()
    except:
        return iter([('::wooey/default', parser)])
    
    



