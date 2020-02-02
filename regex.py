#!/usr/bin/python3
"""
function that match the coincidences in an array
"""
import re
from word2number import w2n
import sys

text = '(zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|teen|fifty|ty|een|y|hundred|thousand|million)'
input_ = sys.argv[1]


regex = re.findall(text, input_)
#print(regex)
joined = ' '.join(regex)
e = w2n.word_to_num(joined)
# print("{:s}".format(input_))
print(e)