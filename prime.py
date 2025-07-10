p_num = int(input("Enter a number: "))
if p_num > 1:
    for i in range(2, p_num-1):
        if p_num % i == 0:
            print("Not a prime number")
            break
    else:
        print("this is a prime number")
else:
    print("this is not a prime number")
