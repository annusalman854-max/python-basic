# Arrays in python:
# an array is acollection of elements of the same datatype stored in a contionuos memory loaation.
# Arrays are used to store mutiple values in a single variable.
# saves memory
# array VS list:
# importing the module.

# #arrays in python:
import array as arr

# #creating an array:
# Number = arr.array("i",[1,2,3,4,5]) 
# print(type(Number))

# # i = integer
# # f = float
# # u = string

# # Accessing array elements.
# print(Number[0]) #1
# print(Number[3]) #4
# print(Number[-1]) #5

# # Adding an element in array:
# # append()
# Number.append(7)
# print(Number)

# #insert()
# number.insert(2,6)
# print(Number)

#deleting an alements:
numbers = arr.array('i',[1,2,3,4,5])
#Remove():
numbers.remove(5)
print(numbers)


