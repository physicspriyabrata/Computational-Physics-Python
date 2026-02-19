#checking even or odd number by entering by users

num=float(input("enter a number__"))
num_char=type(num)
if(num%2==0):
	print("this number is a 'Even' number")
elif(num%2==1):
	print("this number is 'Odd'")
elif(num_char==float):
	print("this number is not for choose even or odd because this is irrational number")
