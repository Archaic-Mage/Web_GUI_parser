from wooey import *
import argparse

@wooey
def cli(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', help='foo help', metavar='FOO')
    parser.add_argument('--bar', help='bar help', metavar='BAR')
    args = parser.parse_args()
    print(args)
    
cli("--foo 1 --bar 2")
