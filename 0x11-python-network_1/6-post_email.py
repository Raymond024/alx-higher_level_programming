#!/usr/bin/python3
"""Script Sends a POST request to a given URL with a given email.
   Usage: ./6-post_email.py <URL> <email>
   Displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
