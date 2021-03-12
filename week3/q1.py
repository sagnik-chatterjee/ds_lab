'''
Author: Sagnik Chatterjee 
Program to find the factos of a given number (input from user)
using for loop.
'''

def factors(n:int):
    list1=[]
    for i in range(2,n):
        if n%i==0:
            list1.append(i)
    return list1

def main():
    n=int(input("Enter the number: "))
    if n >=1:
    	print("Factors of the number are: ")
    	print(factors(n))

    else:
    	print("Please enter a positive natural number for checking tis factors.")

if __name__=='__main__':
	main()

