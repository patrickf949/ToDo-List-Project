#This file manages user accounts
accounts ={}
#dictionary where key is password &value is User

def add_account(name, password):
	#Adds key value pair to the accounts dictionary
	#param: name & password
	#return: n/a
	accounts[password]=name
	#create account
	print("Account created\n")
	print("Enter")
	print("1. To proceed with login")
	print("2. To quit\n")
	num = raw_input()
	if num=='1':
		print("\nHello {0}!\nYou are logged in".format(name))
		return '1'
	else:
		return '0'
	
def login(name, password):
	#Evaluates if the password and 
	#corresponding name exist in the accounts dictionary
	#with option of adding new account & reentering password
	#param: name & password
	#return: n/a
	
	if name in accounts.values():
		if password in accounts.keys():
			if name==accounts.get(password):
				print("Hello {0}!\nYou are logged in".format(name))
				return '1'
		
		# for item in accounts:
		# 	if item[1]==name:
		# 		listOfKeys.append(item[0])

		# if(password in listOfKeys):
		# 	print("Hello {0}!\nYou are logged in".format(name))
		
		else:
			print("\nInvalid password")
			num = raw_input("Press\n1. To Re enter only Password\n2. To Re enter all details\n3. To quit\n")
			if num=='1':
				password1=raw_input("Enter password: ")
				login(name,password1)
			elif num=='2':
				re_enter_details()
			else:
				print('Ts NOT OK to give up!')
				return 0
				
	else:
		print("\nInvalid username")
		print("Press\n1. To Create a new account\n2. To Retry\n3. To quit\n")
		num = raw_input()
		print(num)
		if num=='1':
			add_account(name,password)
			return '1'
		elif num=='2':
			re_enter_details()
		else:
			return 0

def re_enter_details():
	#re enter your username and password
	#param: n/a
	#return: n/a
	name1=raw_input('Enter username: ')
	password1=raw_input('Enter password: ')
	login(name1,password1)




