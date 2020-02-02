


if kwargs:
    for key, value in kwargs.items():
        if key !=




            text = '(zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|teen|fifty|ty|een|y|hundred|thousand|million)'
            input_ = sys.argv[1]
            result = 0
            try:
                if input_ == result:
                    print(result)
                else:
                    print("incorrect!")
                    break
            except Va
                # print("that's not a valid answer. Enter an integer")
                if text:
                    x = re.findall(text, input)
                joined = ' '.join(x)
                # print(joined)
                input = w2n.word_to_num(joined)
                # print(input)
                # print(x, str(sys.argv[1]))
                # print("input = "+ str(input))
                print(str(input))


#!/usr/bin/python3
"""
function that match the coincidences in an array
"""
import re
from word2number import w2n
import sys

text = '(zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|teen|fifty|ty|een|y|hundred|thousand|million)'
input_ = sys.argv[1]
value = (int(sys.argv[1]))

try:
    if value:
        print(value)
    else:
        print('type again')
except:
    pass
    """
    regex = re.findall(text, input_)
    print(regex)
    joined = ' '.join(regex)
    e = w2n.word_to_num(joined)
    # print("{:s}".format(input_))
    print(e)
    """

try:
    if value:
        print(value)
except:
    if text:
        regex = re.findall(text, input_)
        print(regex)
        joined = ' '.join(regex)
        e = w2n.word_to_num(joined)
        # print("{:s}".format(input_))
        print(e)

# value = (int(sys.argv[1]))
input_ = sys.argv[1]
try:
    pass
except:
    if input_ == int:
        print(int)
else:
    text = '(zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|teen|fifty|ty|een|y|hundred|thousand|million)'
    regex = re.findall(text, input_)
    # print(regex)
    joined = ' '.join(regex)
    e = w2n.word_to_num(joined)
    # print("{:s}".format(input_))
    print(e)

#!/usr/bin/python3
"""
function that match the coincidences in an array
"""
import re
from word2number import w2n
import sys


# value = (int(sys.argv[1]))
input_ = sys.argv[1]
try:
    if input_ == int:
        print(int)
except:
    pass
else:
    text = '(zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|teen|fifty|ty|een|y|hundred|thousand|million)'
    regex = re.findall(text, input_)
    if regex:
        joined = ' '.join(regex)
        e = w2n.word_to_num(joined)
        # print("{:s}".format(input_))
        print(e)
    else:
        print(input_)


    def match_numbers(*args):
        input_ = sys.argv[1]
        # input_2 = sys.argv[2]
        try:
            return int(input_)
        except ValueError:
            text = '(zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|teen|fifty|ty|een|y|hundred|thousand|million)'
            regex = re.findall(text, input_)
            if regex:
                joined = ' '.join(regex)
                e = w2n.word_to_num(joined)
                # print("{:s}".format(input_))
                print(e)
            else:
                return None