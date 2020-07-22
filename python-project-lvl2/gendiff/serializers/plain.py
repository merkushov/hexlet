"""
    The package implements the specific functionality
    of serializing Diff data into a Plain structure.
    It looks like a textual description of the identified
    changes.
"""

from gendiff.config import ADDED, CHANGED, EQUAL, NESTED, REMOVED


def process(data, parent=''):
    """Serializes data structure to text. Recursive function"""

    result = ''
    for key in sorted(data.keys()):
        nested_key = parent + '.' + key if parent else key
        string = ''
        node = data[key]

        if node[0] == ADDED:
            string = 'Setting "{}" added with value "{}".\n'.format(
                nested_key, node[1])
        elif node[0] == CHANGED:
            string = 'Setting "{}" changed from "{}" to "{}".\n'.format(
                nested_key, node[1][0], node[1][1])
        elif node[0] == EQUAL:
            pass
        elif node[0] == NESTED:
            string = process(node[1], nested_key)
        elif node[0] == REMOVED:
            string = 'Setting "{}" deleted.\n'.format(nested_key)

        if string:
            result = result + string

    return result
