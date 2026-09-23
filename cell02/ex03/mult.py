n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the second number : "))
re = n1 * n2
print(f"{n1} x {n2} = {re}")

if re > 0:
    print("The result is postitive")
elif re < 0:
    print("The result is negative")
else:
    print("The result is postitive and negative")