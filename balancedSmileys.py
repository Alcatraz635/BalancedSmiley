import sys
import re

test_cases = open(sys.argv[1], 'r')

def smiley(line):
    line = filter(lambda x: x.isalpha() == False, line)
    line = filter(None, list(line.strip()))
    for char in line:
        if char == '(':
            if ')' in line[line.index(char)::]:
                line.remove(char)
                line.remove(')')
    line = ''.join(line)
    line = line.replace(':)', '')
    line = line.replace(':(', '')
    line = line.translate(None, ' :')
    if(len(line) > 0):return False
    else: return True

for test in test_cases:
    print smiley(test)

test_cases.close()
exit(0) 