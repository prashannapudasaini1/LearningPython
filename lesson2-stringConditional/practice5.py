#  WAP to check whether a number is multiple of 7 or not

num = int(input("Enter a number: "))
if num % 7 == 0:
    print(f"{num} is a multiple of 7")
else:
    print(f"{num} is not a multiple of 7")