'''
    This module contains everything related to receivint data
    from a remote source
'''

import requests


def fetch_data_by_url(url: str) -> str:
    r = requests.get(url)
    return r.text
