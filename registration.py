#!/usr/bin/env python

import requests

token = '24d2eed680663fd4ac466f9483466faf'
github = 'https://github.com/knwachuk/code2040'

def main():

    r = requests.post("http://challenge.code2040.org/api/register",
                      data={'token': token, 'github': github})
    print(r.status_code, r.reason)

if __name__ == '__main__':
    main()
