
def template(n1,n2,n3,n4,n5,n6): 

	number1 = n1*1.0 #this gets the first number from the user and stores it in a memory location called number1 
	number2 = n2*1.0
	number3 = n3*1.0 
	number4 = n4*1.0 
	number5 = n5*1.0 
	number6 = n6*1.0 
	total = 480
	list1 = [number1,number2,number3,number4,number5,number6]
	min = 999
	for i in list1:
		if i < min:
			min = i
	print min
	if min == 0:
		average = ((number1+number2+number3+number4+number5+number6-min)/480-min)*100
	average = ((number1+number2+number3+number4+number5+number6-min)/480)*100
	
	result = average
	return result 
     
     
