# traversing a list:
# accesing the element using the loop
# using for loop
# cars = ["ALto", "G-wagonr", "city", "s-presso"]
# # index   0        1        2       3
# # iterating only index of list
# l=len(cars) #5
# for i in range(0,l):
#     print(cars[i])
# #iterating the values in the list
# for car in cars:
#     print(car)
    
# adding elements using for loop
# a=[10,20,30,40,50]
# list1=[]
# n=int(input("enter the number of items:"))
# for i in range(n):
#     v=int(input("enter the item:"))
#     list1.append(v)
# print(list1)

# # give the input values to the list from 0 to 10
# list1=[]
# n=int(input("enter the number of items:"))
# for i in range(n):
#     # v=int(input("enter the item:"))
#     list1.append(i)
# print(list1)

# sum of list items = 10 20 30 40 50 with using sum ().
# a = [10,20,30,40,100]
# sum = 0
# for i in a:
#     sum = sum + i
# print(sum)

# b = [a,b,c,d]
# sum=10
# sum =sum+10
# print(a)
# for i in a:
#      sum = sum + i
# print(sum)

# numbers= [45,23,67,89,12,5,90,34]
# max_num = numbers[0]
# min_num = numbers[0]
# for num in numbers:
#     if num>max_num:
#         max_num=num
#     if num<min_num:
#         min_num=num
# print("maximum number is:",max_num)
# print("minimum number is:",min_num)

#searching for an element in a list
# names = ["fazal","vivek","netaji","arhaan",]
# Searching_name = input("enter the name to be found:")
# found = False 
# for i in names:
#     if Searching_name == i:
#         found=True
#         if found:
#             print("yes")
# else:
#     print("no")

# count even and odd numbers
# numbers = [7,10,12,17,23,31,45,227,229]

# evn_cnt = 0 #2
# odd_cnt = 0 #1

# for i in range(len(numbers)):
#     if numbers[i]%2 == 0:
#         evn_cnt += 1
#     else:
#         odd_cnt += 1
# print("number of even numbers are:",evn_cnt)
# print("number of odd numbers are: ",odd_cnt)
 #reversing a list without reverse
 
# list1 = [7,10,12,17,28,23,31,45,227,229]
# l = len(list1)
# r_list = []
# for i in range(l-1,-1,-1):
#     r_list.append(list[i])
# print(r_list)

#multiply each element in the list
list1 = [7,10,12,17,28,23,31,45,227,229]
m=int(input("enter the number to be multiplied:"))
After_multipilaction = []
for i in list1:
    After_multipilaction.append(i*m)
print(After_multipilaction)

    