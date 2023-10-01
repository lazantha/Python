for i in range(5):
	for j in range(5):
		if i==3 and j==3:
			print("Found",str(i),str(j))
			break;
		print(f'Row:{i} | {j}')
	else:
		continue;
		print('Else met')
	print("Break")
	break;
