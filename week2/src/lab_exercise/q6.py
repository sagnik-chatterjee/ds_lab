x=int(input("ENter the start number (for prime range) : "))
y=int(input("Enter the end number (for prime range): "))

print("Prime numbers between", x, "and", y, "are:")

for i in range(x, y + 1):
   if i > 1:
       for j in range(2, i):
           if (i % j) == 0:
               break
       else:
           print(i,end='\n')


