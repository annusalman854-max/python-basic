
#conversions
#km->m
dis = 25#m
km = dis/1000
m = dis*1000
cm = dis*100
print(km)
print(m)
print(cm)
#find the number wheather it is even or odd
#even=0,2,4,6,8,......
#odd=1,3,5,7,9,.......
number=int(input("enter a number"))
if number%2==0:
    print("number is even")
else :
    print("number is odd")

#voter=major,minor
age=int(input("enter the age: "))
if age >= 18:
    print("major,eligible for vote")
else:
    print("minor,not eligible vote")

#leap year or not
leap = int(input("enter the year:"))
if leap%4==0 and leap%100==0 or leap%400==0:
    print("it is leap year,")
elif leap %100!=0:
    print("it is a leap year:")
else:
    print("it is not a leap year.")

