import os

paragraph = "\n\n"

# same as input but with formatting
def prompt(prompt : str):
    return input("{}: ".format(prompt))

# return string with spaces to specified indent level
def indent(indent_level : int) -> str:
    s = ""
    for _ in range(indent_level):
        s += "    "
    return s

def indent_all(indent_level : int, lines):
    res = lines.copy()
    for i in range(len(res)):
        res[i] = indent(indent_level) + res[i]
    return res