#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == '__main__':
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body_response = response.read()
        print(f"Body response:\n\t- type: {type(body_response)}\n\
    \t- content: {body_response}\n\
    \t- utf8 content: {body_response.decode('utf-8')}")
