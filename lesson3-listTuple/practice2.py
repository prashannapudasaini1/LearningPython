#  WAP to check if a list is palindrome or not
list1 = [1,2,3,2,1]
copy_list1 = list1.copy()

copy_list1.reverse()

if copy_list1 == list1:
    print("list1 is a palindrome")
else:
    print("list1 is not a palindrome")
    