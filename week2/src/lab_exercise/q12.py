list1=[123,-456,789,-987,654,-321,-21345]
count_pos=0
count_neg=0
for i in list1:
	if i>0:
		print(f"Positive number found in list is : {i}")
		count_pos+=1
	elif i<0:
		print(f"Negative number found in list is :{i}")
		count_neg+=1
	else:
		print("Zeroes found in list , at index ")

print(count_pos)
print(count_neg)
