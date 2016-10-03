#!/usr/bin/env python

import requests

token = '24d2eed680663fd4ac466f9483466faf'

def registration():

    github = 'https://github.com/knwachuk/code2040'

    r = requests.post("http://challenge.code2040.org/api/register",
                      data={'token': token, 'github': github})
    print(r.status_code, r.reason)

def reverse_str():
    
    r = requests.post("http://challenge.code2040.org/api/reverse",
                      data={'token': token})

    # Making sure it is a string
    if (isinstance(r.text, basestring)):
        reverse_str = str(r.text[::-1])

    r = requests.post("http://challenge.code2040.org/api/reverse/validate",
                      data={'token': token, 'string': reverse_str})
    print r_status_code, r.reason

def main():

    # Current position in the application process
    step_position = 2

    if (step_position == 1):
        registration()

    elif (step_position == 2):
        reverse_str

if __name__ == '__main__':
    main()
