import random

def invert(string):
    list_random = random.sample(range(0, len(string)), len(string)//2)
    ret_str = ''
    for i in range(len(string)):
        if i in list_random:
            # ret_str += str(chr(~ord(string[i])))
            # print(chr(~ord(string[i])))
            print(i)
        else:
            ret_str += str(string[i])
    return ret_str
