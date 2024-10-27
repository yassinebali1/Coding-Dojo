my_new_favorite_language = 'Python'  # variable declaration, initialize string
num1 = 42  # variable declaration, initialize number
num2 = 2.3  # variable declaration, initialize float
boolean = True  # variable declaration, initialize boolean
string = 'Hello World'  # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  # variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  # variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana')  # variable declaration, initialize tuple
print(type(fruit))  # log statement, type check
print(pizza_toppings[1])  # access value, list
pizza_toppings.append('Mushrooms')  # add value, list
print(person['name'])  # access value, dictionary
person['name'] = 'George'  # change value, dictionary
person['eye_color'] = 'blue'  # add value, dictionary
print(fruit[2])  # access value, tuple

if num1 > 45:  # conditional, if
    print("It's greater")  # log statement
else:  # conditional, else
    print("It's lower")  # log statement

if len(string) < 5:  # conditional, if, length check
    print("It's a short word!")  # log statement
elif len(string) > 15:  # conditional, else if, length check
    print("It's a long word!")  # log statement
else:  # conditional, else
    print("Just right!")  # log statement

for x in range(5):  # for loop, start, stop
    print(x)  # log statement
for x in range(2, 5):  # for loop, start, stop
    print(x)  # log statement
for x in range(2, 10, 3):  # for loop, start, stop, increment
    print(x)  # log statement
x = 0  # variable declaration, initialize number
while(x < 5):  # while loop, start, stop
    print(x)  # log statement
    x += 1  # increment

pizza_toppings.pop()  # delete value, list
pizza_toppings.pop(1)  # delete value, list

print(person)  # log statement
person.pop('eye_color')  # delete value, dictionary
print(person)  # log statement

for topping in pizza_toppings:  # for loop, sequence
    if topping == 'Pepperoni':  # conditional, if
        continue  # control flow, continue
    print('After 1st if statement')  # log statement
    if topping == 'Olives':  # conditional, if
        break  # control flow, break

def print_hello_ten_times():  # function
    for num in range(10):  # for loop, start, stop
        print('Hello')  # log statement

print_hello_ten_times()  # function call

def print_hello_x_times(x):  # function, parameter
    for num in range(x):  # for loop, start, stop
        print('Hello')  # log statement

print_hello_x_times(4)  # function call, argument

def print_hello_x_or_ten_times(x=10):  # function, parameter with default value
    for num in range(x):  # for loop, start, stop
        print('Hello')  # log statement

print_hello_x_or_ten_times()  # function call
print_hello_x_or_ten_times(4)  # function call, argument

"""
Bonus section
"""

# print(num3)  # log statement, variable not defined (NameError)
# num3 = 72  # variable declaration, initialize number
# fruit[0] = 'cranberry'  # change value, tuple (TypeError)
# print(person['favorite_team'])  # access value, dictionary (KeyError)
# print(pizza_toppings[7])  # access value, list (IndexError)
# print(boolean)  # log statement
# fruit.append('raspberry')  # add value, tuple (AttributeError)
# fruit.pop(1)  # delete value, tuple (AttributeError)
