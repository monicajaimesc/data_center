#!/usr/bin/python3
"""
function that will split strings into text and number
"""

re = ['foofo21', 'bar432', 'foobar12345']
match = re.match(r"([a-z]+)([0-9]+)", 'foofo21', re.I)
if match:
    items = match.groups()
    # items is ("foo", "21")

