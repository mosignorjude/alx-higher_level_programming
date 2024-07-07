#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
import requests
import sys

if __name__ == '__main__':

    r = requests.get(sys.argv[1])
    headers = r.headers
    # convert headers to dictionary for easier access
    h_dict = dict(headers)
    h_var = h_dict.get("X-Request-Id")
    print(h_var)
