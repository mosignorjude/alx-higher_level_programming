#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""
import urllib.request
import sys

if __name__ == '__main__':
    data = f"email={sys.argv[2]}"
    data = data.encode('ascii')
    url = sys.argv[1]
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        content = response.read()
        print(content.decode('utf-8'))
