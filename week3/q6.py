'''
Author : Sagnik Chatterjee 
Program to find element wise product between 2 matrices
'''

import numpy as np 


def main():
	try:
		print("Assuming a 2d matrix")
		print('Enter the dimension of the 1st matrix(column and row),seperated using a single space on the same line')
		n,m=map(int,input().split())
		arr1=[[int(input()) for x in range(n)] for y in range(m)]
		
		print('Enter the dimension of the 2nd matrix(column and row),seperated using a single space on the same line')
		a,b=map(int,input().split())
		arr2=[[int(input()) for x in range(a)] for y in range(b)]
		
		if(n!=a or m!=b ):
			raise Exception("Dimension do not match for the two matrices;please check your values.")

		numpy_arr1=np.array(arr1)
		numpy_arr2=np.array(arr2)

		##the original matrices 
		print("The first matrix is :- ")
		print(numpy_arr1)
		print("The second matrix is :- ")
		print(numpy_arr2)

		## the element wise product of the 2 matrices 
		print("The element wise product of the two matrices are:- ")
		print(np.multiply(numpy_arr1,numpy_arr2))

	except Exception as e:
		print(e)


if __name__=='__main__':
	main()