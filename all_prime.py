first_p = int(input("Enter the first number: "))
end_p = int(input("Enter the second number: "))

for p_no in range(first_p, end_p + 1):
    if p_no > 1:
        for i in range(2, p_no-1):
            if p_no % i == 0:
                break 
        else:
            print(p_no ," is a prime number")   
