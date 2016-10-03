#!/usr/bin/env python

import requests
import datetime

token = '24d2eed680663fd4ac466f9483466faf'

def registration():

    github = 'https://github.com/knwachuk/code2040'

    r = requests.post("http://challenge.code2040.org/api/register",
                      data={'token': token, 'github': github})
    print r.status_code, r.reason

def reverse_str():
    
    r = requests.post("http://challenge.code2040.org/api/reverse",
                      data={'token': token})

    # Making sure it is a string
    if (isinstance(r.text, basestring)):
        reverse_str = str(r.text[::-1])

    r = requests.post("http://challenge.code2040.org/api/reverse/validate",
                      data={'token': token, 'string': reverse_str})
    print r.status_code, r.reason

def needle_haystack():

    r = requests.post("http://challenge.code2040.org/api/haystack",
                      data={'token': token})

    # Finding needle in haystack! :)
    haystack = r.json()

    # for key in haystack.keys(): # Not NEEDED! Already know the names of the keys
    # Also note that API expects indexes to start counting at 0
    needle = haystack['needle']
    needle_index = haystack['haystack'].index(needle)

    r = requests.post("http://challenge.code2040.org/api/haystack/validate",
                      data={'token': token, 'needle': needle_index})
    print r.status_code, r.reason

def prefix():

    r = requests.post("http://challenge.code2040.org/api/prefix",
                      data={'token': token})

    words = r.json()
    len_pref = len(words['prefix'])

    non_prefixed = [str(word) for word in words['array'] if word[0:len_pref] != words['prefix']]

    payload = {'token': token, 'array': non_prefixed}
    r = requests.post("http://challenge.code2040.org/api/prefix/validate",
                      json=payload)
    print r.status_code, r.reason

def dating_game():
    
    r = requests.post("http://challenge.code2040.org/api/dating",
                      data={'token': token})

    dating = r.json()

    iso_8601_datestamp = '%Y-%m-%dT%H:%M:%SZ'
    time = datetime.datetime.strptime(dating['datestamp'], iso_8601_datestamp)
    new_time = time + datetime.timedelta(seconds=dating['interval'])
    
    # Verifying output
    # print dating['datestamp'], new_time.strftime(iso_8601_datestamp), dating['interval']
    # print time, datetime.timedelta(seconds=dating['interval']), new_time

    payload = {'token': token,
               'datestamp': new_time.strftime(iso_8601_datestamp)}
    r = requests.post("http://challenge.code2040.org/api/dating/validate",
                      json=payload)
    print r.status_code, r.reason
    
def main():

    # Current position in the application process
    step_position = 5

    if (step_position == 1):
        registration()

    elif (step_position == 2):
        reverse_str()

    elif (step_position == 3):
        needle_haystack()

    elif (step_position == 4):
        prefix()

    else:
        dating_game()

if __name__ == '__main__':
    main()
