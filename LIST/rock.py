import random

com_choice=random.randint(0,2)
user_choice=int(input("Enter choice !"))

if com_choice>user_choice:
	print(f'computer win ! computer choice:{com_choice} and your choice {user_choice} ')
elif com_choice<user_choice:
	print(f'You win ! computer choice:{com_choice} and your choice {user_choice} ')
else:
	print(f'DROW ! computer choice:{com_choice} and your choice {user_choice} ')


