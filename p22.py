import re
import sys
import math

#returns the int value of a name
def name_value(name):
    base = ord('A') - 1
    answer = 0
    for letter in list(name):
        answer += ord(letter) - base
    return answer


if __name__ == "__main__":
    f = open('names.txt', 'r')
    names = f.read()

    #strips the files into a list of names
    sorted_names = [name.strip('"') for name in names.split(',')]
    sorted_names.sort()
    answer = 0
    for index in range(len(sorted_names)):
        answer+= (index+1) * name_value(sorted_names[index])
    print answer
    sys.exit()

