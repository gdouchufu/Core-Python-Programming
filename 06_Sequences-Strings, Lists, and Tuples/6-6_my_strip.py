#!/usr/bin/env python
import string

def my_string_strip(_str):
    if len(_str) <= 0:
        return _str

    # left strip
    while _str[0] == ' ':
        _str = _str[1:len(_str)]
    # right strip
    while _str[len(_str)-1] == ' ':
        _str = _str[0:len(_str)-1]

    return _str

print my_string_strip('   asdf asdf   ')