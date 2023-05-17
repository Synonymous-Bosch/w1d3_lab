def return_10():
    return 10

def add(num1, num2):
    result = num1 + num2
    return result

def subtract(num1, num2):
    result = num1 - num2
    return result

def multiply(num1, num2):
    result = num1 * num2
    return result

def divide(num1, num2):
    result = num1 / num2
    return result

def length_of_string(a_string):
    result = len(a_string)
    return result

def join_string(string1, string2):
    result = string1 + string2
    return result

def add_string_as_number(string1, string2):
    result = int(string1) + int(string2)
    return result 

def number_to_full_month_name(month_number):
    result = None
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    for month in months:
        if months.index(month) == month_number - 1:
            result = month
    return result   
    
def number_to_short_month_name(month_number):
    result = None
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for month in months:
        if months.index(month) == month_number - 1:
            result = month
    return result   

def volume_of_cube(side_length):
    result = side_length * side_length * side_length
    return result

def reverse_string(a_string):
    result = a_string[::-1]
    return result

def fahrenheit_to_celsius(fahrenheit):
    result = (fahrenheit - 32) * (5 / 9)
    return result