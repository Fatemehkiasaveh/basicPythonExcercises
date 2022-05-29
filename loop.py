
# i = 1
# while i<=10:
#     print(i)
#     i+=1

# for i in range(6):
#     for j in range(1,i):
#         print(j,end=' ')

#     print('')

#Exercise 3: Calculate the sum of all numbers from 1 to a given number
# n = int(input('Enter a number'))
# sum = 0
# for i in range(n+1):
#     sum = i + sum
# print(sum)

# n = int(input('Enter a number:'))
# result = sum(range(1, n+1))
# print(result)

#Exercise 4: Write a program to print multiplication table of a given number
# n = 2
# for i in range(1,11):
#     p=2*i
#     print(p)

#Exercise 5: Display numbers from a list using loop

# numbers = [12, 75, 150, 180, 145, 525, 50]

# for number in numbers:
#     if number>500:
#         break
#     elif number>150:
#         continue
#     elif number%5==0:
#         print(number)

 #Exercise 6: Count the total number of digits in a number
# num = 7324
# count = 0
# while num>0:
#     num = num //10
#     count += 1
    
# print(count)

#Exercise 7: Print the following pattern
# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j, end=' ')
#     print('')
       
# for i in range(0,6):
#     for j in range(5-i, 0, -1):
#         print(j, end=' ')
#     print('') 
    
#Exercise 8: Print list in reverse order using a loop
#solution1
# list1 = [10, 20, 30, 40, 50]
# new_list = reversed(list1)
# for item in new_list:
#     print(item)

#solution2
# list1 = [10, 20, 30, 40, 50]
# size = len(list1)
# for i in range(size-1,-1,-1):
#     print(list1[i])

#Exercise 9: Display numbers from -10 to -1 using for loop

# for i in range(10,0,-1):
#     print(-i)
#Exercise 10: use else block to display a message 'Done' after succsessful excuation of for loop

# for i in range(5):
#     print(i)
# else:
#      print('Done!')

#Exercise 11: Write a program to display all prime numbers within a range

# start = 25
# end = 50
# for num in range(start,end+1):
#     if num>1:
#         for i in range(2,num):
#             if (num%i==0):
#                 break
#         else:
#             print(num)

#Exercise 12: Display Fibonacci series up to 10 terms
# num1 = 0
# num2 = 1
# for num in range(9):
#     res = num1 + num2
#     print(num1, end=' ')
#     num1 = num2
#     num2 = res

#Exercise 13: Find the factorial of a given number
# factorial = 1
# n = 5
# for i in range(1,n+1):
#     factorial = factorial *i

# print(factorial)

# num = 5
# factorial = 1
# if num < 0:
#     print("Factorial does not exist for negative numbers")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
#     # run loop 5 times
#     for i in range(1, num + 1):
#         # multiply factorial by current number
#         factorial = factorial * i
#     print("The factorial of", num, "is", factorial)

#Exercise 14: Reverse a given integer number
# num = 9876 
# revers_num = 0
# while num>0:
#     reminder= num % 10
#     revers_num = (revers_num*10)+ reminder
#     num = num//10
# print(revers_num)

#Exercise 15: Use a loop to display elements from a given list present at odd index positions

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(my_list[1:10:2])

# for item in my_list[1:10:2]:
#     print(item, end=' ')

#Exercise 16: Calculate the cube of all numbers from 1 to a given number

# number = int(input('Enter a number:'))
# print('the current number is:', number)
# cube = number * number * number
# print('the cube is: ', cube)

# n = 6
# for i in range(1,n+1):
#     cube = i*i*i
#     print('The current number is: ',i, 'and the cube is: ', cube)
   
#Exercise 17: Find the sum of the series upto n terms
# n = 5
# sum = 0
# start = 2
# for num in range(n):
#       sum = sum + start
#       start = start*10+2

# print(sum)
# print(2, end='+')

#Exercise 18: Print the following pattern
# for i in range(5):
#     for j in range(i+1):

#         print('*', end= '')
    
#     print('\r')
 
# for i in range(5,0,-1):
#     for j in range(0,i-1):
#         print('*', end='')

#     print('\r')
# number1 = int(input('Enter the first number:'))
# number2 = int(input('Enter the second number:'))
# result = number1*number2
# print('The result is:', result)

# print('Name', 'is', 'James', sep='**')

# num = 8
# print(oct(num))
# print('%o'% num)

# num = 458.541315
# print('%.2f'% num)

# [78.6, 78.6, 85.3, 1.2, 3.5]

# numbers = []
# for i in range(5):
#     number = float(input('Enter a num:'))
#     numbers.append(number)
# print(numbers)

#Exercise 6: Write all content of a given file into a new file by skipping line number 5


# fp = open(r'C:\Users\Asus\Desktop\work\text.txt', 'r')
# with open('text.txt','r') as fp:
#     lines = fp.readlines()
# with open('newtext.txt', 'w') as fp:
#     count = 0 
#     for line in lines:
#         if count==4:
#             count+=1
#             continue
#         else:
#             fp.write(line)

#         count+=1

# Name1, Name2, Name3 = input('Enter three string').split()
# print('Name1:', Name1)
# print('Name2:', Name2)
# print('Name3:', Name3)


# print('I have {} dollars so I can buy {} football for {:.2f} dollars'.format
# (1000, 3, 450))

# import os
# size = os.stat('text.txt').st_size
# if size==0:
#     print('file is empty')
# else:
#     print(size)

# with open('text.txt','r') as fp:
#     lines = fp.readlines()
#     print(lines[2])