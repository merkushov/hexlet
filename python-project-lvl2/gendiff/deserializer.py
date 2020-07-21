import os
import json
import yaml


def _open_json_file(filepath):
    return json.load(open(filepath))


def _open_yaml_file(filepath):
    return yaml.safe_load(open(filepath))


def process(filepath):
    data = {}

    root, ext = os.path.splitext(filepath)
    if (ext in ('.json', '.jsn')):
        data = _open_json_file(filepath)
    elif (ext in ('.yml', '.yaml')):
        data = _open_yaml_file(filepath)
    else:
        raise Exception("Unsupported input format")

    return data
