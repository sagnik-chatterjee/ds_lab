'''
Author : Sagnik Chatterjee 
Program to transpose a given matrix.
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

	# the transpose of the matrix is 
	print("The transpose of the matrix is :-")
	print(numpy_arr.transpose())

if __name__=='__main__':
	main()