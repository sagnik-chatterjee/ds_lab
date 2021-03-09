##part 1 
## create array from list with type float 
import numpy as np 
p=[123.45,567.89,12.877,123123.3333]

arr =np.array(p)

print("Array created from list ")
print(type(arr))
print(arr)


##part 2 

tup1=(11,22,43,23523,1231213)
arr2 =np.array(tup1)

print("Array created from tuple")
print(type(arr2))
print(arr2)

##part3 
##creating a array of zeroes 
a=(3,4)
print(np.zeros(a))

##part 4 
##craete a sequence of integers from 0 to 20 with sttep of 5

for i in range(0,20):
    print(i,end=' ')
    i+=5
print(" ")    
##part 5 
#reshapeing 3*4 array to 2*2* 3 array 

arr3= np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
print(arr3.shape)
arr4= arr3.reshape(2,2,3)
print(arr4)
print(arr4.shape)


##part 6 
arr4=np.array([[1,2,3],
               [4,5,6],
               [7,8,9],
               [10,11,12],
               [13,14,15]])

##sum of the elements 
print(arr4.sum())

#maximum along the horizoantal and the vertical 
print(np.amax(arr4,axis=1))
print(np.amax(arr4,axis=0))

#minimu alogn the horizontal and vertical 
print(np.amin(arr4,axis=1))
print(np.amin(arr4,axis=0))


