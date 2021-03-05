print("List functions and operations ")

list1=[]

for i in range(1,101):
	#adding eleemnts to the list 
	list1.append(i)
##extend the list 
list1.extend([123,567])

##insert any  elemnt at the given index

list1.insert(90,213213)


#pop any element form the list 

list1.pop(100)

## return the pons of the first item of the list that has a value of x 
print(list1.index(100))

