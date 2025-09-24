# # Tuples
# #examples:
# coondinates = ("x","y")
# my_tuple = (10,20,30)
# print(my_tuple)
# print(type(my_tuple))

# #creating atuple:
# #empty tuple
# emy = ()
# #Tuple with number
# N = (1,2,3,4,5,6,7)
# # Tuple with strings
# s = ("A","B","C","a","b","c")
# # Tuples with mixed datatypes
# M = (24,3.24,"A","C",True,"Falese")
# # Tuples with single elements:
# a = 10 #Int
# print(type(a))
# b = [10] # list
# print(type(b))
# c = (10,20)
# print(type(c))

# # Accessing Elements:
# # Tuple uses index values to acces am element.
# A = (10,20,30,40)
# #i    0  1  2  3
# #-i   -4 -3 -2 -1
# print(A[0]) #10
# print(A[1]) #20
# print(A[2]) #30
# print(A[3]) #40
# print(A[-1]) #40
# print(A[-2]) #30
# print(A[-3]) #20
# print(A[-4]) #10


# #slicing the tuple:
# #Extract part of the tuple using start index and end index
# #([start index: end index])
# A = (10,20,30,40)
# #i    0  1  2  3
# #-i  -4 -3 -2 -1
# print(A[1:3]) #20 30 40
# print(A[:2]) # 10 20 30 
# print(A[-1:-3])
# print(A[:3])

# # Changing the values:
# #Tuple are immutable,so cannot change the value.
# A[1] = 50
# print(A)# typeError: 'tuple' object does not support item assingnment
# # append():
# A.append(50)
# print(A)

# Length:
# max:
# min:
# sum:

#concetinnation:
#Repetation:

# Searching and Checking:
# print(40 in a)
# print(30 not in a)
# # in operater:
# # not in operater:
# # index():
# print(a.count(30))
# # count():
# print(a.count(40))

#copying
a = (10,20,30,40)
b = tuple(a)
print(b)




