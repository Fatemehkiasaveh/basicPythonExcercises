#Variable lengh arguments 
# def func1(*numbers):
#     for no in numbers:
#         print(no)
# func1(20,40,60)

# def calculation(a,b):
#     sum = a + b
#     subs = a - b
#     return(sum,subs)
# res = calculation(30,20)
# print(res)

# def show_employee(name, salary=9000):
#     print(name, salary)

# show_employee('Ben')
# show_employee('Jessica',1200)

#Exercise 5: Create an inner function to calculate the addition in the following way

# def outer_func(a,b):
#     def addition(a,b):
#         return a + b
#     add = addition(a,b)
#     return add + 5
# print(outer_func(10,10))

#Exercise 6: Create a recursive function


# a = range(0,11)
# x = print(sum(a))

# def addition(num):
#     if num:
#         return num + addition(num-1)
#     else:
#         return 0
# res = addition(10)
# print(res)

#Exercise 7: Assign a different name to function and call it through the new name
# def student_display(name, age):
#     print(name,age)

# showStudent = student_display
# showStudent('Marzieh', 21)



# a =  list(range(4,29,2))
# print(a)

x = [4, 6, 8, 24, 12, 2]
b = max(x)
print(b)