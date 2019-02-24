def write_output(num):
    digit_array, total_sum = [], 0
    if num == 0:
        print(num)
        return
    elif num < 0:
        print("Enter only positive integers")
    try:
        for i in range(1,5):
            digit_array.append(num*i)
        for i in digit_array:
            total_sum += int(i)
        print("Sum of the numbers is = %d"%(total_sum))
    except:
        print("Enter only integers")

write_output(input("Enter a number : "))