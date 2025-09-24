# # functions:
# # syntex:
# # same task eithout function:
# name = "salman shah" # here name is input varible (parameter) and "salman shah" is value to the parameter (argement)
# print ("hello",name)

# #Type of function arguments:-
#  # A positional argument:- when we pass arguments in the same order as the function parameter.
# def greet (name<rollno):
#     print("hello",name,"your rollno is",roll no )
# greet("salman shah","L6")
# greet ("L6",salman shah) 

# # B) key word arguments:- when we pass values or arguments by writing the parameter(variable = value), they are called as keyword arguments.add()
# def greef (rool no,name):
#     print("hello",name,"your rollno is",rollno)
# greet (name = "salman shah",rollno = "L6")    

# # C) Default arguments:-
# def greet (name = "student"):
#     print("hello",name)
# greet()#hello student
# greet("salman shah")#hello salman shah
# greet()

# # D) variable-lenth argumenth:  
# list1 = 10,20,30,40,50
# def sum1(*list1):
# for i in range(len(list1)):
#     sum2 = sum1+list[i]
#     print(sum2)
#     print(type(list1))
#     sum(10,20,30,40,50)

# # 2.kwargs:
# def datails(**info):
#     for i,j in info.items():
#         print(i,":",j)
# details(name = "salmann",rollno = "h4",branch = "csm")

#factorial
def factortial(fact):
    fact = 1
    for i in range(5,0,-1):
        fact = fact+i
        print(fact)
factorial(5)
factorial(4)

#recursive:
def Rfactorial(n):
    if n == 0
    retun Rfactorial(n-1)
Rfactorial(5)






