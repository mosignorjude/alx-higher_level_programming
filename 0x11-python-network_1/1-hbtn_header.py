#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
if __name__ == '__main__':
    import urllib.request
    import sys

    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as response:
        headers = response.headers
        # convert headers to dictionary for easier access
        h_dict = dict(headers)
        h_var = h_dict['X-Request-Id']
        print(h_var)
