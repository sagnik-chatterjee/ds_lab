import numpy as np 
arr =np.array([[1,23,45,67],[56,7,8,10]])

print("Sum along the row")
print(np.sum(arr,1,np.int32))

print("Sum along the column")
print(np.sum(arr,0,np.int32))
