# THIS PROGRAM IS TO FIND THE FIRST 10 MULTIPLES OF A NUMBER
num = int(input("Enter the number you wish to find the multiples of: "))


for i in range(1, 11):
    print(num, "*", i, "=", num * i)