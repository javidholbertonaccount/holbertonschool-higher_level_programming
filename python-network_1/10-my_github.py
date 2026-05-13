#!/usr/bin/python3
"""Takes GitHub credentials and uses the GitHub API to display the id"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    print(response.json().get('id'))
