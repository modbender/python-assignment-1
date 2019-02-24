import math

def write_output(c,d,h):
    print(math.sqrt(2*c*d)/h)

try:
    c = int(input("Enter the value of c : "))
    d = int(input("Enter the value of d : "))
    h = int(input("Enter the value of h : "))
    write_output(write_output(c,d,h))
except:
    print("Enter a integer value")