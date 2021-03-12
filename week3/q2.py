'''
Author : Sagnik Chatterjee
Program to find the sum of columns and rows using axis.

'''

import numpy as np


def main():
	print("Assuming a 2d matrix")
	print('Enter the dimension of the column and row,seperated using a single space on the same line')
	n,m=map(int,input().split())
	arr=[[int(input()) for x in range(n)] for y in range(m)]
	numpy_arr=np.array(arr)

	#original matrix 
	print("Original matrix is :- ")
	print(numpy_arr)

	##summing along all the rows 
	print("The sum of all the rows:")
	print(np.sum(numpy_arr,axis=1))

	#summing along all the cols
	print("The sum of all the cols:-")
	print(np.sum(numpy_arr,axis=0))

	#sum of matrix 
	print("Total sum of all elements of the array:- ")
	print(np.sum(numpy_arr))

if __name__=='__main__':
	main()