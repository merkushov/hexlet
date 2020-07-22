"""
    The package implements the specific functionality
    of serializing Diff data into the Dictionary structure.
    It looks like this:
      * added items are marked with "+"
      * deleted items are marked with "-"
"""

import json


def process(data):
    return json.dumps(data, indent=4)
