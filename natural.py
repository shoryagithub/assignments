natural_no1 = int(input("Enter a first natural number: "))
natural_no2 = int(input("Enter a second natural number: "))
total = sum(range(natural_no1, natural_no2 + 1))
print("Sum of all natural numbers between", natural_no1, "and", natural_no2, "is:", total)