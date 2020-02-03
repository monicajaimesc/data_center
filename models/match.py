#!/usr/bin/python3
"""
function that match the coincidences in an array
"""
import re
from word2number import w2n
import sys


def match_numbers(input_):

    try:
        return int(input_)
    except ValueError:
        text = '(zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|teen|fifty|ty|een|y|hundred|thousand|million)'
        regex = re.findall(text, input_)
        if regex:
            joined = ' '.join(regex)
            e = w2n.word_to_num(joined)
            # print("{:s}".format(input_))
            return e
        else:
            return None


def main():
    print(match_numbers(sys.argv[1]))


if __name__ == "__main__":
    main()

