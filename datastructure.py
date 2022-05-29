# from audioop import reverse
# list1 = [100, 200, 300, 400, 500]
# list1.reverse()
# print(list1)
#Exercise 2: Concatenate two lists index-wise
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# list3 = [i+j for i, j in zip(list1,list2)]
# print(list3)
#Exercise 3: Turn every item of a list into its square
# numbers = [1, 2, 3, 4, 5, 6, 7]
# squer = []
# for number in numbers:
#     number = number * number
#     squer.append(number)
# print(squer)
#solution2
# numbers = [1, 2, 3, 4, 5, 6, 7]
# res = [x*x for x in numbers]
# print(res)
#Exercise 4: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# res = [x+y for x in list1 for y in list2]
# print(res)
#Exercise 5: Iterate both lists simultaneously
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# for x,y in zip(list1, list2[::-1]):
#     print(x,y)
#Exercise 6: Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# # res = []
# # for i in list1:
# #     if i:
# #         res.append(i)
# # print(res)
# res = list(filter(None, list1))
# print(res)
#Exercise 7: Add new item to list after a specified item
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)
#Exercise 8: Extend nested list by adding the sublist
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# # sub list to add
# sub_list = ["h", "i", "j"]
# list1[2][1][2].extend(sub_list)
# print(list1)
#Exercise 9: Replace list’s item with new value if found
# list1 = [5, 10, 15, 20, 25, 50, 20]
# index = list1.index(20)
# list1[index]=200
# print(list1)
#Exercise 10: Remove all occurrences of a specific item from a list.
# list1 = [5, 20, 15, 20, 25, 50, 20]
# val = 20
# #solution1
# def remove_val(sample_list,val):
#     return [i for i in sample_list if i != val]
# res = remove_val(list1, val)
# print(res)
#solution2
# while 20 in list1:
#     list1.remove(20)
# print(list1)


#Exercise 1: Convert two lists into a dictionary

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

#soloution1

# mydict = dict(zip(keys,values))
# print(mydict)

#soloution2
# dict1 = dict()
# for i in range(len(keys)):
#     dict1.update({keys[i]:values[i]})
# print(dict1)

#Exercise 2: Merge two Python dictionaries into one

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict1.update(dict2)
# print('Updated dictionary:')
# print(dict1)

#Exercise 3: Print the value of key ‘history’ from the below

# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }

# print(sampleDict["class"]["student"]["marks"]["history"])

#Exercise 4: Initialize dictionary with default values

# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}

 
# res = dict.fromkeys(employees, defaults)
# print(res)
# print(res['Kelly'])

#Exercise 5: Create a dictionary by extracting the keys from a given dictionary

 


# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # # Keys to extract
# keys = ["name", "salary"]

# # #solution1
# res = dict()

# for k in keys:
#     res.update({k:sample_dict[k]})
# print(res)
 
# #solution2
# keys = ["name", "salary"]
# newDict = {k:sample_dict[k] for k in Keys}
# print(newDict)

#Exercise 6: Delete a list of keys from a dictionary

 
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# # Keys to remove
# keys = ["name", "salary"]

 
# #1
# for k in keys:
#     sample_dict.pop(k)
    
# print(sample_dict)

#2
# sample_dict = {k:sample_dict[k] for k in sample_dict.keys() - keys}
# print(sample_dict)

#Exercise 7: Check if a value exists in a dictionary
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# # for k in sample_dict.keys():
# #     if sample_dict[k]==200:
# #         print('200 is present in this dict')
# if 200 in sample_dict.values():
#     print('200 is in this dict')

# Exercise 8: Rename key of a dictionary

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
# sample_dict.pop('city')
# print(sample_dict)
# sample_dict.update({'location':'New york'})
# print(sample_dict)
#2
# sample_dict['location']= sample_dict.pop('city')
# print(sample_dict)

#Exercise 9: Get the key of a minimum value from the following dictionary#

# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }

# print(min(sample_dict, key=sample_dict.get))

#Exercise 10: Change value of a key in a nested dictionary
# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }
# sample_dict['emp3']['salary'] =8500
# print(sample_dict)
