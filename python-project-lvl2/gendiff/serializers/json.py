"""
    The package implements the specific functionality
    of serializing Diff data into a JSON structure
"""

import json


def process(data):
    return json.dumps(data, sort_keys=True, indent=4)
