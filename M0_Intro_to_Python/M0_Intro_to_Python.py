# Exercise 5.1 - Conditional Executional: Modify this code so that it does apply both discounts when both conditions are True.
birthday_is_today = True
number_of_items = 10
price = 10.00

if birthday_is_today and number_of_items > 5:
    price = price * 0.85 * 0.9
elif birthday_is_today:
    price = price * 0.85
elif number_of_items > 5:
    price = price * 0.9

# print(price)

# Exercise 5.2 - Write a function that takes a string as input and returns the middle character of the string. If there is no middle character, return None instead.
# E.g. your_function('abcd') should return None and your_function('abcde') should return 'c'

def middle_letter(word):
    length = len(word)
    if length%2 == 0 :
        return None
    return word[length//2]

# print(middle_letter('None'))
# print(middle_letter('Loved'))

# Exercise 5.3 - Loops: Add together all of the numbers in a list (without using the built-in sum function) For example, given this line of code, can you write code that will print 100?

number_list = [5, 15, 30, 50]
def list_total(number_list):
    total = 0
    for i in number_list:
        total += i
    return total

# print(list_total(number_list))

# Exercise 5.4 - Loops: Write a function, find_strings_containing_a, which takes a list of strings and returns just the ones containing the letter ‘a’. So after you define the function, the following code should print ['some cats', 'a dog'] to the terminal.

# def find_strings_containing_a(list):
#     a_list = []
#     for i in list:
#         if 'a' in i:
#             a_list.append(i)
#     return a_list        
def find_strings_containing_a(list):
    return [i for i in list if 'a' in i ]
full_list = ['the mouse', 'some cats', 'a dog', 'people']
result = find_strings_containing_a(full_list)
# print(result)

# Exercise 5.5- Loops: Write a function that prints a piece of text 100 times. But please use a for loop and a range, rather than copying and pasting the print statement 100 times.

def repeat_100(word):
    for i in range (100):
        print(word)
# repeat_100('Hi')

# Exercise 5.6 - Loop: Write a function that takes a positive integer n, and returns the sum total of all square numbers from 1 squared to n squared (inclusive).
# For example, with n = 3 your function should return 14 (equal to 1 + 4 + 9)

def sum_of_square_root(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**2
    return sum
print(sum_of_square_root(3))

# Exercise 5.7 - Loops: Can you make this code print just A, B and C, by adding some code before the print statement? Don’t modify the two lines of code already there, just add some more lines of code before the line print(letter)

for letter in ['A', 'B', 'X', 'C', 'D', 'E']:

    if letter == 'D':
        break
    elif letter == 'X':
        continue
    print(letter)
    