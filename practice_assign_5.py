# question 1 Write a python script to remove the last digit from a given number. (for example, if user enters 2534 then your output should be 253)

number = int(input("enter your number"))
number = int(number/10)
print(number)

# question 2 Write a python script to get the last digit from a given number. (for example, if user enters 2089 then your output should be 9)

number = int(input("enter your number"))
number = int(number%10)
print(number)

# question 3 Write a python script to swap data of two variables

number_1 = int(input("enter a number"))
number_2 = int(input("enter a number"))

number_1,number_2 = number_2,number_1
print(number_1)
print(number_2)

# question 4 Write a python script to find x power y, where values of x and y are given by user

number = int(input("enter your number"))
power = int(input("enter your power"))

power_x = number**power

print (power_x)

# question 5 Write a python script which takes a three digit number from the user and displays only its first digit.

number = int(input("enter your number"))
number = int(number/100)
print(number)

# question 6 Write a python script which takes a three digit number from the user and displays only its middle digit.

number = int(input("enter your number"))
number = int(number/10)
number = (number %10)
print(number)

# question 7 Write a python script which takes a three digit number from the user and displays only its last digit.

number = int(input("enter your number"))
number = int(number%10)
print(number)

# question 8 Write a python script to use IN operator to display the data present in the list

l1=[1,2,3,4,5,6,7,8,9,10]

number = int(input("enter your number"))
print(number in l1)

# question 9 Write a python script to use NOT IN operator to display the data not present in list

l1=[1,2,3,4,5,6,7,8,9,10]

number = int(input("enter your number"))
print(number not in l1)

# question 10 Write a python script to use IS operator to display if both variables are the same object or not?

l1 = [1,2,3,4,5,6]
l2 = [1,2,3,4,5,6]

result_1 = l1 is l2
result_2 = l1 is not l2
print(result_1)
print(result_2)
