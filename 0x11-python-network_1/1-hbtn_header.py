#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys

if __name__ == '__main__':

    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
        # headers = response.headers
        # convert headers to dictionary for easier access
        # h_dict = dict(headers)
        # h_var = h_dict['X-Request-Id']
        # print(h_var)
