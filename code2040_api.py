#!/usr/bin/env python

import datetime

import requests

from settings import github_url, token


def registration(github: str) -> None:
    """Registration function for Code2040."""
    r = requests.post("http://challenge.code2040.org/api/register",
                      data={'token': token, 'github': github})
    print(r.status_code, r.reason)


def reverse_str() -> None:
    """reverse_str function for Code2040."""
    r = requests.post("http://challenge.code2040.org/api/reverse",
                      data={'token': token})

    if (type(r.text) is str):       # Making sure it is a string
        reverse_str = str(r.text[::-1])

    r = requests.post("http://challenge.code2040.org/api/reverse/validate",
                      data={'token': token, 'string': reverse_str})
    print(r.status_code, r.reason)


def needle_haystack() -> None:
    """needle_haystack function for Code2040."""
    r = requests.post("http://challenge.code2040.org/api/haystack",
                      data={'token': token})

    haystack = r.json()             # Finding needle in haystack! :)

    # for key in haystack.keys(): # Not NEEDED! Already know the names of the keys
    # Also note that API expects indexes to start counting at 0
    needle = haystack['needle']
    needle_index = haystack['haystack'].index(needle)

    r = requests.post("http://challenge.code2040.org/api/haystack/validate",
                      data={'token': token, 'needle': needle_index})
    print(r.status_code, r.reason)


def prefix() -> None:
    """prefix function for Code2040."""
    r = requests.post("http://challenge.code2040.org/api/prefix",
                      data={'token': token})

    words = r.json()
    len_pref = len(words['prefix'])

    non_prefixed = [str(word) for word in words['array']
                    if word[0:len_pref] != words['prefix']]

    payload = {'token': token, 'array': non_prefixed}
    r = requests.post("http://challenge.code2040.org/api/prefix/validate",
                      json=payload)
    print(r.status_code, r.reason)


def dating_game() -> None:
    """dating_game function for Code2040."""
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
    print(r.status_code, r.reason)


def main():

    # Current position in the application process
    step_position = 5

    if (step_position == 1):
        registration(github_url)

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
