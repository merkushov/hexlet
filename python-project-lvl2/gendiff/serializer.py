"""
    The module is an interface to the objects of
    Data Serialization into a text representation.
"""

import gendiff.serializers.dictionary
import gendiff.serializers.json
import gendiff.serializers.plain


def process(data, output_format):
    if output_format == 'dictionary':
        return gendiff.serializers.dictionary.process(data)
    elif output_format == 'json':
        return gendiff.serializers.json.process(data)
    elif output_format == 'plain':
        return gendiff.serializers.plain.process(data)
    else:
        raise Exception("Unsupported output format")

    return ''
