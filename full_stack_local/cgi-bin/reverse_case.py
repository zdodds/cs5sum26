#!/usr/bin/env python3

import os
import sys
import cgi

def reverse_capitalization(text):
    return text.swapcase()

form = cgi.FieldStorage()
input_text = form.getfirst("text", "")
result = reverse_capitalization(input_text)

print("Content-Type: text/plain")
print()
print(result)
