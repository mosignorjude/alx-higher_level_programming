#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email_value = sys.argv[2]
    data = {'email': email_value}
    r = requests.get(url, data)
    content = r.text
    print('Your email is: {}'.format(content))
