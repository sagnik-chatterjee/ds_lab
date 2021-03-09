from typing import List 

def factors(n:int)->List:
    list1=[]
    for i in range(2,n):
        if n%i==0:
            list1.append(i)
            
    return list1


def main():
    n=int(input("Enter the number: "))
    print("Factors of the number are: ")
    print(factors(n))
    
main()

