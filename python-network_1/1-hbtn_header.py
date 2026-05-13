#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.getheader('X-Request-Id'))
