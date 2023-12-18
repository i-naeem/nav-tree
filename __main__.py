#! /usr/bin/python

from traverser import traverse
from utils import get_nav, print_tree

nav = get_nav("https://mycodelesswebsite.com/")
items = traverse(nav)

print_tree(items)
