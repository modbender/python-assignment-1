def fact(num):
    return 1 if num == 0 else num*fact(num-1)

try:
    print(fact(int(input("Enter number : "))))
except:
    print("Enter a non negative integer value")