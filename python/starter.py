import random
# single line comment
"""
multi line
comments

hello world with import for random number i guess
"""

def main():
    # string.format helps you to place variables in the message
    print("hello there {}".format(random.randint(0,9)))

# there you have it this is barebones basic python 3

# basic for all python code 
# call a function determined as main 
# if python is called directly and not as module

if __name__=="__main__":
    main()