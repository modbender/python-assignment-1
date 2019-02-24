def write_output(num):
    if num <= 0:
        print("Enter a value greater than 0")
    for i in range(1,num+1):
        print("%d:%d"%(i,i*i))

try:
    write_output(int(input("Enter a number : ")))
except:
    print("Enter a integer number that is greater than 0")