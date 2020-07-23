"""
    The package implements the specific functionality
    of serializing Diff data into the Dictionary structure.
    It looks like this:
      * added items are marked with "+"
      * deleted items are marked with "-"
"""

from gendiff.config import ADDED, CHANGED, EQUAL, NESTED, REMOVED

INDENT_DEFAULT = 4


def process(data, indent=0):
    """
        Serializes data structure to a formated dictionary.
        Recursive function
    """

    local_indent = (indent + INDENT_DEFAULT) * ' '
    local_indent_with_sign = (indent + INDENT_DEFAULT - 2) * ' '

    result = '{\n'
    for key in sorted(data.keys()):
        string = ''
        node = data[key]

        if node[0] == ADDED:
            string = '{}+ "{}":{},\n'.format(
                local_indent_with_sign,
                key,
                node[1]
            )
        elif node[0] == CHANGED:
            string = '{}- "{}":{},\n'.format(
                local_indent_with_sign,
                key,
                node[1][0]
            )
            string = string + '{}+ "{}":{},\n'.format(
                local_indent_with_sign,
                key,
                node[1][1]
            )
        elif node[0] == EQUAL:
            string = '{}"{}":{},\n'.format(
                local_indent,
                key,
                node[1]
            )
        elif node[0] == NESTED:
            string = '{}"{}":'.format(
                local_indent,
                key
            )
            string = string + process(node[1], indent + INDENT_DEFAULT)
        elif node[0] == REMOVED:
            string = '{}- "{}":{},\n'.format(
                local_indent_with_sign,
                key,
                node[1]
            )

        if string:
            result = result + string

    result = result + (indent * " ") + '}\n'
    return result
