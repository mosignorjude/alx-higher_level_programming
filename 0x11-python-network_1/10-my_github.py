#!/usr/bin/python3
"""A script that:
- takes in your GitHub credentials (username and password)
- and uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    auth = HTTPBasicAuth(username, passwd)
    url = "https://api.github.com/user"

    r = requests.get(url, auth=auth)
    print(r.json().get("id"))
