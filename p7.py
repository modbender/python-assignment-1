import re

def write_output(s):
    uppl = lowl = 0
    for i in s:
        if re.match(r'^([A-Z])',i):
            uppl+=1
        if re.match(r'^([a-z])',i):
            lowl+=1
    print("Count of\n    Upper Case Letters = %d\n    Lower Case Letters = %d"%(uppl,lowl))

write_output(input("Enter a string : "))