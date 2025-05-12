# WAP to enter marks of 3 subjects from the user and store them in a dictionary.
# Start with an empty dictionary and then add the subjects and marks to it.

dict ={}

subject1 = input("Enter the first subject name: ")
marks1 = int(input("Enter the marks of the first subject: "))
subject2 = input("Enter the second subject name: ")
marks2 = int(input("Enter the marks of the second subject: "))
subject3 = input("Enter the third subject name: ")
marks3 = int(input("Enter the marks of the third subject: "))

dict[subject1] = marks1
dict[subject2] = marks2
dict[subject3] = marks3

print(dict)