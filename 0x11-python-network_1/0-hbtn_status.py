#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request
body_response = ''
url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    body_response = response.read()

print(f"Body response:\n"
      f"    - type: {type(body_response)}\n"
      f"    - content: {body_response}\n"
      f"    - utf8 content: {body_response.decode('utf-8')}")
