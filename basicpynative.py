#Calculate the multiplication and sum of two numbers

from ast import While
from http.client import ImproperConnectionState
from itertools import count
from math import remainder
import numbers
from re import I
# from readline import write_history_file
from numpy import character, integer, product


# def calculate(number1, number2):
#     product = number1 * number2
#     if product > 1000:
#         result = number1 * number2
#         print('The result is:', result)

#     else:
#         result = number1 + number2
#         print('The result is:', result)

# number1 = 40
# number2 = 30
# calculate(number1, number2)

# def multiplication_or_sum(num1, num2):
#     product = num1 * num2
#     if product >1000:
#         return product
#     else:
#         return num1 + num2

# result = multiplication_or_sum(20,30)
# print('The result is:', result)
# result = multiplication_or_sum(30,40)
# print('This result is:', result)


#Exercise 2: Print the sum of the current number and the previous number

# for i in range(10):
#     sum = i + (i+1)
#     print('current number:',i+1, 'previous number:', i, 'sum:', sum)

# previous_number = 0
# for i in range(10):
#     print('current number:', i, 'previous number:', previous_number, 'sum', i+previous_number)
#     previous_number = i


#Exercise 3: Print characters from a string that are present at an even index number

# word = input('Enter word:')
# print('the original word is:', word) 
# size = len(word)
# print('only even index chars:')
# for i in range(0,size-1,2):
#      print('index[' ,i, ']', word[i])

# word = input('Enter word:')
# print('The original word is:', word)
# x = list(word)
# for i in x[0::2]:
#     print(i)
#Exercise 4: Remove first n characters from a string
# word = input('Enter a word:')
# n = int(input('Enter n:'))

# def remove_chars(word, n):
#     size = len(word)
#     if n< size:
#          new_string = word[n:]
#          print(new_string)
#     else:
#         print('n is out of range')

# remove_chars(word,n)

# def remove_chars(word,n):
#     print('the original string is:', word)
#     x = word[n:]
#     return x
 
# print('the removing characters from a string')
# print(remove_chars('pynative', 4))
# print(remove_chars('pynative', 2))
     
#Exercise 5: Check if the first and last number of a list is the same

# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]
# def my_func(list):
#     if list[0]==list[-1]:
#         return True
#     else:
#         return False

# print('Given list:', numbers_x, 'result is:',my_func(numbers_x))

# print('Given list:', numbers_y, 'result is:',my_func(numbers_y))

#Exercise 6: Display numbers divisible by 5 from a list
# def devisible(list):
#     print('Given list is:', list)
#     for x in list:
#         y = x % 5
#         if y==0:
#             print(x)
# my_list =  [10, 20, 33, 46, 55]
# devisible(my_list)

# num_list = [10, 20, 33, 46, 55]
# print('Given list:', num_list)
# for num in num_list:
#     if num%5==0:
#         print(num)

#Exercise 7: Return the count of a given substring from a string
# str_x = "Emma is good developer. Emma is a writer"
# print('Emma appeared',str_x.count('Emma'), 'times')

# def substring(statement, target):
#     statement = input('Enter statement:')
#     target = input('Enter a target:')
#     print(target, 'appeard', statement.count(target), 'times')
    
# statement = str_x = "Emma is good developer. Emma is a writer"
# target = 'is'
# substring(statement, target)

#Exercise 8: Print the following pattern

# for i in range(6):
#     for j in range(i):
#         print(i, end=' ')
#     print("")
        
#Exercise 9: Check Palindrome Number

# def palindrome_num(number):
#     original_num = number
#     print('original number', number)
#     reverse_num = 0
#     while number > 0:
#         reminder = number%10
#         reverse_num = (reverse_num*10)+reminder
#         number = number//10

#     if original_num==reverse_num:
        
#         print('The number given is palindrome')
#     else:
        
#         print('The given number is not palindrome')

# palindrome_num(1221)

#Exercise 10: Create a new list from a two list using the following condition

# result_list = []
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# for item in list1:
#     if item % 2 !=0:
#         result_list.append(item)

# for num in list2:
#     if num % 2 == 0:
#         result_list.append(num)

# print('the result list is', result_list)

# def merge_list(list1,list2):
#     result_list = []
#     for num in list1:
#         if num % 2 !=0:
#             result_list.append(num)

#     for num in list2:
#         if num % 2 ==0:
#             result_list.append(num)
#     return result_list

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# print('The result is', merge_list(list1, list2))

#Exercise 11: Write a Program to extract each digit from an integer in the reverse order.

# number = int( input('Enter a number:'))
# while number > 0:
    
#     digit = number % 10
    
#     number = number // 10
#     print(digit, end=" ")

#Exercise 12: Calculate income tax for the given income by adhering to the below rules

# def calculate_income(income):
#      if income <= 10000:
#          print('You dont need to pay tax')
#      elif income>20000 and income < 30000:
#          first = income - 10000 
#          tax = first * 10 / 100
#          print(' your tax is', tax)
#      elif income>30000:
#         first = income - 10000 
#         tax_first = first * 10 / 100
#         second = income - 20000
#         tax_second = second *20 /100
#         tax = tax_first + tax_second
#         print('your tax is ', tax)

# income = 45000
# payable_tax = 0
# if income<=10000:
#     payable_tax=0
# elif income<=20000:
#     x = income -10000
#     payable_tax = x* 10 /100
# else:
#     payable_tax = 0
#     payable_tax = 10000* 10/100
#     payable_tax+= (income-20000)*20/100
# print('the payable tax is:', payable_tax)

#Exercise 13: Print multiplication table form 1 to 10
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j, end=' ')
#     print('')

#Exercise 14: Print downward Half-Pyramid Pattern with Star (asterisk)
# for i in range(6,0,-1):
# #     for j in range(i,0,-1):
# #         print('*', end='')

# #     print('')

#Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# def exponent(base, exp):
#     result = base ** exp
#     return result
# print(exponent(2,3))

# def exponent(base, exp):
#     num = exp
#     result = 1
#     while num > 0:
#         result = result * base
#         num = num - 1
#     print(base, 'raises to the power ', exp, 'is: ', result)

# exponent(2,5)