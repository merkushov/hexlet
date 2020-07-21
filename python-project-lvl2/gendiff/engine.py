__version__ = '0.1.3'

import gendiff.deserializer
import gendiff.serializer
from gendiff.config import ADDED, CHANGED, EQUAL, NESTED, REMOVED


def diff_between_files(file1, file2):
    return diff_between_data(
        gendiff.deserializer.process(file1),
        gendiff.deserializer.process(file2)
    )


def diff_between_data(data1, data2):
    """
        The main method of the package. Looks for
        the difference between two data structures.
    """
    all_keys = data1.keys() | data2.keys()
    common = {}
    if isinstance(data1, dict) and isinstance(data2, dict):
        for key in all_keys:
            val1 = data1.get(key, None)
            val2 = data2.get(key, None)

            if val1 and val2:
                if isinstance(val1, dict) and isinstance(val2, dict):
                    common[key] = (NESTED, diff_between_data(val1, val2))
                elif val1 == val2:
                    common[key] = (EQUAL, val1)
                else:
                    common[key] = (CHANGED, (val1, val2))
            else:
                if val1:
                    common[key] = (REMOVED, val1)
                else:
                    common[key] = (ADDED, val2)
    else:
        # raise Exception("Unsupported data type")
        pass

    return common


def format(data, format):
    return gendiff.serializer.process(data, format)
