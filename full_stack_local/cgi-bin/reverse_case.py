#!/usr/bin/env python3

import os
import sys
from urllib.parse import parse_qs


def reverse_capitalization(text):
    return text.swapcase()


content_length = int(os.environ.get("CONTENT_LENGTH", "0"))
request_body = sys.stdin.read(content_length)
form = parse_qs(request_body)
input_text = form.get("text", [""])[0]
result = reverse_capitalization(input_text)

print("Content-Type: text/plain")
print()
print(result)
