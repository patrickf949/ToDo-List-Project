list11=['a','b','c','d','e',0,1,0,0,'f','g','h',False,False,'i','j' ]

def sorts_list(listt):
	numbers = []
	others = []
	for i in listt:
		if(type(i)==int):
			numbers.append(i)
		else:
			others.append(i)
		# if(isinstance(i,(int))):
		# 	a=i
		# 	print(a)
		# 	listt.remove(a)
		# 	print(a)
		# 	listt.append(a)
		# 	print(a)
		 
		# try:
		# 	i = i + 1
		# 	number = i - 1
  #   		numbers.append(number)
  #   		# listt.append(i)
		# except:
		# 	others.append(i)
		# 	print("not integer")


	print(others + numbers)


sorts_list(list11)
