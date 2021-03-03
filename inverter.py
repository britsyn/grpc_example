import random

def invert(string):
    bin_str = ' '.join(format(ord(x), 'b') for x in string if x!= ' ')
    random_numbers = random.sample(range(0, len(bin_str)), len(bin_str)//2)
    ib_string = ''
    for i in range(len(random_numbers)):
        if i in random_numbers:
            if bin_str[i] == "1":
                ib_string += "0"
            elif bin_str[i] == "0":
                ib_string += "1"
            else:
                ib_string += " "
        else:
            ib_string += str(bin_str[i])
    return ib_string
