import re

def write_output(s):
    digits = letters = schars = sps = 0
    for i in s:
        if re.match(r'^(\d)',i):
            digits+=1
        if re.match(r'^([a-zA-Z])',i):
            letters+=1
        if re.match(r'^(?![a-zA-Z\d\s])',i):
            schars+=1
        if re.match(r'^(\s)',i):
            sps+=1
    print("Number of letters = %d\nNumber of digits = %d\nNumber of special sharacters = %d\nNumber of spaces = %d\n"
        %(letters, digits, schars, sps))

write_output(input("Enter a string : "))