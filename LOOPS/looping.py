#for in loop
list_=[1,2,3,4,5]
name="lasantha"
# for letters in name:
# 	print(letters)

numbers=[1,2,3,4,5,6,7]
sqlist=[]

# for numbers in numbers:
# 	square=numbers**2
# 	sqlist.append(square)
# print(sqlist)


#for else loop (else part run only when loop was executed successfully)
# for numbers in numbers:
# 	if numbers==3:
# 		break
# else:
# 	print("Successfully terminated !")

# print("Loop currupted while running Not runnig else statement")


# value=int(input("Enter total number of items: "))
# numberList=[]
# count=0
# total=0

# for i in range(1,value+1):
# 	value_list=int(input("Enter Values: "))
# 	numberList.append(value_list)
# 	count=count+1

# for numbers in numberList:
# 	total=total+numbers
# else:
# 	print(f'Sum of the Elements: {total}\n Average Of the Element: {total//count}')


# numberList=[]

# for i in range(0,5):
# 	values=int(input("Eneter Numbers: "))
# 	numberList.append(values)


# maxi=numberList[0]
# mini=numberList[0]

# for numbers in numberList:
# 	if numbers>maxi:
# 		maxi=numbers
# 	if numbers<mini:

# 		mini=numbers
# else:
# 	print(f'Maximum: {maxi} \n Minimum: {mini}')


# for i in range(2,5):
# 	print(i)
# 	

#FizzBuzz

# for i in range(1,15+1):

# 	if i%3==0 or i%5==0:
# 		print('FizzBuzz')
# 	elif i%3==0:
# 		print('Fizz')
# 	elif i%5==0:
# 		print('Buzz')
	
# 	else:
# 		print(i)
# 		

#while loop

print("Enter 0 for exit: ")


total=0
while True:
	value=int(input("Enter Values For Summing: "))
	if value==0:
		break
	total+=value
print(total)



