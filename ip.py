import logging
import requests


def get():
    r = requests.get('http://ifconfig.co/ip')
    if r.status_code == 200:
        return r.text.strip()
    else:
        return None