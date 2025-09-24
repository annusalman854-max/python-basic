#collection data types
#list1 = [10,20,30,40,50] #integer values
#fruits = ["apple","banana","mango"] #STRINGS values
#list2 = [10.1,20.2,30.3,40.4,50.5] #float values
#list3 = [True,False,True,True] #boolean value
#list4 = [10,20.5,"hello",True,"False"] #multi data types value
#output
#print(list2)

#example: 0 1 2 3 4 ...n-1
#list1 = [10,20,30,40,50]
#print(list1[0])
#print(list1[1])
#print(list1[2])
#print(list1[3])
#print(list1[4])

#by negative values
#print(list1[-1])
#print(list1[-3])
#print(list1[-4])

#slicing
#str = ["prabhas","balayya","PSPK","bob","bhai"]
#print(str[:3])
#print(str[1:4])
#print(str[-3:])

#append:
#kalkicast=["prabhas","kamal h",]
#kalkicast[1] = ("sandeep R V")
#print("kalkicast")

#searching and checking:
#in operator
# a = [2,4,6,8,10,12,14]
# if 2 in a:
#     print("yes item is present in the list")

#not in operater:
##print(3 not in a)

#index method(): 
#print(a.index(10))#4
 
#count():
# a = [2,4,6,8,10,12,14]
# cnt = 0
# print(a.count(8))
# for i in range(10):
#     if i == 8:
#         cnt = cnt + 1
# print(cnt)

#sorting: sort()
# st = [25,12,5,31,13,18,7,45,8,55,68]
# st.reverse()#68,55,8,45,7,18,13,31,5,12,25
# st.sort()
# print(st)#Ao = 5,7,8,12,13,18,25,31,45,55,68
# st.reverse()
# print(st) # DO = 68,55,45,31,25,18,13,12,8,7,5
# st1 = [25,8,4,7,10] #25,10,8,7,4
# st1.sort(reverse = True)
# print(st1)

#copying the list:
# Frd1 = ["A","C","D","A","D","B","B","C","C","A","A"]
# Frd2 = Frd1.copy()
# Frd2[2] = "B" #changing
# print(Frd2)

#Built - in functions eith loos:
# st=[25,12,5,31,13,18,7,45,8,55,68]
# print(len(st))#11
# print(max(st))#68
# print(min(st))#5
# print(sum(st))#287

# #multipli values using input data to the list:
# a = input("enter a multiple values:").split()
# print(a)
# a.sort()
# print(a)
# a.reverse()
# print(a)
# a = list(map(int,input("enter a multiple values:").split))
# print(a)#21,10,22,5,22
# a.sort()
# print(a)
# a.reverse()
# print(a)

#tranversing a list:
# accessing the elements using a loopusing for loop
#

# Adding element using for loop:
# list1=[]
# for list in range(0,5):
#     a = input("value:")
#     list1.append(a)
# print(list1)

# frnds = []
# n = int (input("enter a n value:"))
# for list in range(0,n):
#     a = input("enter a frd:")
#     frnds.append(a)
# print(frnds)

# give the input values to the lists from 0 to 10
# list1 = []
# n = int(input("enter a n value:"))
# for i in range(0,n):
#     a = input("value")
#     list1.append(i)
# print(list1)

# # sum of list items = 10 20 30 40 50 without using sum().
# list1 = [10,20,30,40,50]
# sum = 0
# for i in list1:
#     sum=sum+i
# print(sum)

#convert ["p","y","t","h","o","n"] to python
# list2 = ["p","y","t","h","o","n"]
# str1 = ""
# for i in list2:
#     str1 = str1+i
# print(str1)

# Find the maximum and mimimum number from list without using max() and min().
numbers= [45,23,67,89,12,5,90,34]
max_num = numbers[0]
min_num = numbers[0]
for num in numbers:
    if num>max_num:
        max_num=num
    if num<min_num:
        min_num=num
print("maximum number is:",max_num)
print("minimum number is:",min_num)













