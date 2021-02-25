#1
num=float(input("Enter a number :"))
if num>0:
    print("Pos number")
elif num==0:
    print("0")
else:
    print("Neg number")

#2
x=float(input("Enter a number:"))
if x<100:
    print("Smaller number")
if x>200:
    print("Larger Number")
print("Finished")

#3
x=5
print("Before 5")
if x==5:
    print("This is 5")
    print("Still 5")

print("After 5")
print("Before 6")
if x==6:
    print("This is 6")
print("After 6 ")

#4

x=float(input("Enter a number"))
if x<20:
    print("Below 20")
elif x<10:
    print("Below 10")
else:
    print("Something else")
print("Done")

#5 nested decisions 
x=42
if x>1:
    print("Above one")
    if x<100:
        print("Less than 100")
print("All Done")

#6 Ternay operator
age=15 
b=("kid" if age <18 else "adult")
print(b)

# 7 usage of for loop 
for val in [5,4,3,2,1]:
    print(val)
print("Done")

#8 
stud =['Ram','Vijay',"Nithya","Anu","Ramesh","Suja"]
for k in stud:
    print("Hello",k)
print("Done")

#9 
for i in range(5):
    print(i)
    if i>2:
        print("Bigger than 2")
    print("Done with i",i)

#10 

x=int(input("Enter a number:- "))
for i in range(1,x+1):
    if x%i==0:
        print(i)


# 11 calc the largest number in  a array 
import math
x=[9,41,12,3,74,15]
largest = -12312312
for i in x:
    if i>largest:
        largest=i 
print(largest)

## 12 calc the smallest number in a array 
smallest=132123
for i in x:
    if i<smallest:
        smallest=i 
print(smallest)

##13 clac the count ,sm and the average of the numerical array 

count=sum1=avg=0 

for i in x:
    count=count+1 
sum1=sum(x)
avg= sum1/count 
print(count)
print(sum1)
print(avg)

## 14 filtering in a loop (all ums >20) 
for i in x:
    if i>20:
        print(i )

##15 instead of printing the result ,store the elements in a variable(object)

res=[] 
for i in x:
    if i>20:
        res.append(i)

print(res)

## 16 repalce all elementx <20 into 0 ,store the result in different varibale(object
'''
import numpy as np 
y=np.zeros(len(x))
for i in range(len(x)):
    if x[i] >20 :
        y[i]=x[i]
print(y)
'''






