#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
if __name__ == '__main__':
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        headers = response.getheaders()
        # convert headers to dictionary for easier access
        h_dict = dict(headers)
        h_var = h_dict['X-Request-Id']
        print(h_var)
