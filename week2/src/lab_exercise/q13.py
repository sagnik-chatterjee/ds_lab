list1=[1,23,4,5,67,91,123,345,678,123123,23213,123,4342,1312]

print("The list before removing even elements in list :",list1)
for i in list1:
	if i%2==0:
		list1.remove(i)

print("The list after removing even elements ",list1)
