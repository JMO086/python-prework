# Question 1

def hello_name(user_name):
    print("Hello_" + user_name.upper() + "!")

hello_name('username')

# Question 2

def first_odds(number):
    return [x for x in range(0, number + 1) if x % 1 == 0]

#Question 3

def max_num_in_list(a_list):
    print("Max Number in list: ", a_list[-1])

a_list = [10, 20, 30, 40, 50]

#Question 4

def is_leap_year(a_year):
    leap_year = False

    if (year % 4 == 0) and (year % 100 != 0):
        leap_year = True
    elif (year % 100 == 0) and (year % 400 != 0):
        leap_year = False
    elif (year % 400 == 0):
        leap_year = True
    else:
        leap_year = False

    return leap_year

# Question 5

a_list = [2,3,4,5,6,7]

def is_consecutive(a_list):
    if len(set(a_list)) == len(a_list) and max(a_list) - min(a_list) == len(a_list) - 1:
        return True

    else:
        return False
