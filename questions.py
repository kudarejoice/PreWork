# Question 1 - write a function to print "Hello_Username"

def hello_name(user_name):
    print("Hello" + (user_name.upper()) + "!")

hello_name("Kuda")


# Question 2 - Print first 100 odd numbers in Python.

def odd_num():
    for num in range(101):
        if num % 2 != 0: 
            print(num) 
odd_num()

# Question 3 - Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    print(a_list)

mylist = [1, 2, 3, 4]
max_num_in_list(mylist)

# Question 4 - Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):

    if(a_year % 4 == 0) or (a_year % 100 != 0) and (a_year % 400 == 0):
        print(is_leap_year)
    else:
        a_year = False
        print('(a_year) is False')

is_leap_year(2021)

# Question 5 - Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
       if a_list[i] + 1 == a_list[i + 1]:
           i += 1
       else:
            status = False
            break
    print(status)

