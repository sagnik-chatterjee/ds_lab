'''
Author: Sagnik Chatterjee 
Operations on arrays 
'''
import numpy as np

#part a : Create array from list with type float

print('\nPart a')
print("\nEnter the size of the list ")
p=int(input())
arr1=[]
print('Enter the float values for the list')
while p>0:
	q=float(input())
	arr1.append(q)
	p=p-1
arr =np.array(arr1)
print("\nArray created from list :- \n")
print(arr1)

#part b: Create array from tuple  
print('\nPart b')
tup1=(11,22,43,23523,1231213)
arr2 =np.array(tup1)
print("\nArray created from tuple:- ")
print(arr2)

#part c:- Creating a 3*4 array with all zeroes
print('\nPart c ')
a=(3,4)
print("\nThe 3*4 array created with all zeroes: - \n")
print(np.zeros(a))

#part d:- Creae a sequence of integers fom 0 to 20 with steps of 5 
print('\n Part d ')
temp=0
sequence=[]
while temp<=20:
	sequence.append(temp)
	temp+=5

print('The sequence is :- \n')
print(sequence)


#part e:- Reshape 3X4 array to 2X2X3 array
print('Part e\n')
arr3=np.arange(12).reshape(3,4)
print("\nThe original array :- ")
print(arr3)
print('\nThe reshaped array:- ')
print(arr3.reshape(2,2,3))


''' part f:- Find maximum and minimum element of array, Row wise max and min, column wise max
and min and sum of elements. (Use functions max(), min(), sum())
'''
print('Part f\n')
a=np.arange(12).reshape(2,6)
print('The array is :-\n ',a)
print("Full array Max = " , a.max() , " Min = " , a.min() , " Sum = " , a.sum()) 
print("Rowwise array Max = " , a.max(axis = 1) , " Min = " , a.min(axis = 1) , " Sum= " , a.sum(axis = 1)) 
print("Rowwise array Max = " , a.max(axis = 0) , " Min = " , a.min(axis = 0) , " Sum= " , a.sum(axis = 0)) 