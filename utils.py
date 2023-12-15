"""!
@brief Utility functions for the project.

This contains fucntions for loading the parsing parameters and generating the corresponding HTML forms.
"""

from js import JS
from html import HEAD
from argparse import (ArgumentParser, _SubParsersAction)

def is_subparser(action):
    return isinstance(action, _SubParsersAction)

def get_subparser(actions):
    return list(filter(is_subparser, actions))[0]

def iter_parsers(parser):
    ''' Iterate over name, parser pairs '''
    try:
        return get_subparser(parser._actions).choices.items()
    except:
        return iter([('::wooey::default', parser)])

def parse_gui_args(gui_dict):
    """!
    Parses the form data received from the HTML form and returns the corresponding command line arguments.
    @param gui_dict: Dictionary containing the form data.
    @return: List of command line arguments.
    """
    args = list()
    args_dict = dict()
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

def generate_div(input_type, placeholder, metavar, multiple=False):
    """!
    Generates the HTML code for a single input field.
    """
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

def generate_end_parser(parser, prev_link):
    """!
    Generates the HTML code for the last parser in the chain.
    """
    actions = parser._optionals._actions
    form = f"""<form action="{prev_link}" method="post">\n"""
    # form += f"""<input type="hidden" name="link" value="{prev_link}">\n"""
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

def generate_content(parser, part_idx, parts):
    # generating the previous link 
    prev_link = ''
    for i in range(part_idx):
        prev_link += ('/' + parts[i])
        
    content = "" # remains empty unless ::wooey::default is triggered
    sidebar = "" # remains empty if ::wooey::default is triggered
    next = None
        
    # constructing the sidebars for the current level - marking the active link
    for name, subparser in iter_parsers(parser):      
        if name == '::wooey::default':
            content = generate_end_parser(subparser, prev_link)
        else:
            sidebar += "<div class='sidebar'>\n"
            for name, subparser in iter_parsers(parser):
                if part_idx < len(parts) and name == parts[part_idx]:
                    next = subparser
                    sidebar += f"""<a class='active' href="{prev_link}/{name}" onclick="change_active(this)">{name}</a>\n"""
                else:
                    sidebar += f"""<a href="{prev_link}/{name}" onclick="change_active(this)">{name}</a>\n"""
            sidebar += "</div>\n"
        break
    
    content_div = "<div class='content'>\n"
    
    if content:
        content_div += content
    elif next:
        content_div += generate_content(next, part_idx+1, parts)
        
    content_div += "</div>\n"
    return sidebar + content_div

def generate_form(parser, link):
    parts = link.split('/')[1:]
    content = generate_content(parser, 0, parts)
    return content

def generate_html(parser, link):
    HTML = "<html>\n" + HEAD + "<body>\n" + generate_form(parser, link) + "</body>\n" + JS + "</html>"
    return HTML
    
    



