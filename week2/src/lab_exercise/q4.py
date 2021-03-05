a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))

if c<b<a or b<c<a:
	print(f"the largest number is : {a}")

elif a<c<b or c<a<b:
	print(f"the largest number is : {b}")

elif a<b<c or b<a<c:
	print(f"the largest number is : {c}")
