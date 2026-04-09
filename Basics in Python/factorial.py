#print a factorial of a number input by user (using for loop)
a=int(input("enter a number,that you wnat to print factorial "))
i=1
fact=1
for i in range(a, 0,-1):
	print(i)
	if(i==a):   #once calculate
		for j in range(i, 0, -1):
			fact=fact*j		
print(fact)

print("*******************************************************************************")

#OR
fact=1
for i in range(1,a+1):
	fact=fact*i
print("factorial of number is: ", fact)
