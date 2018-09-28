#This file manages user accounts


accounts ={}
#dictionary where key is password &value is User

client_todos={}
#contains all tasks of clients at the time

current_clientname=[]
#stores the name of the current client

def add_account(name, password):
	"""
	Adds key value pair to the accounts dictionary
	param: name & password
	return: n/a
	"""
	
	if not name in accounts.values():
		accounts[password]=name
		#create account
		print('------------------------------------------------------------------------------------------------------\n')
		add_info_to_all_client_todos(name)
		print("Account created\n")
		print("Enter")
		print("1. To proceed with login")
		print("2.(or any other character) To go to main menu\n")
		num = input()
		if num=='1':
			num1=login(name,password)
			
			print(current_clientname)
			return num1
		else:
			print('------------------------------------------------------------------------------------------------------\n')
			return '0'
	else:
		print('An account with this username already exists ')
		print('Add numbers to differentiate from existing account like')
		print('[{0}323] or any other random numbers or characters'.format(name))
		print('So Press')
		print('1. To proceed login with this account')
		print('2. To re-enter your details')
		print('3. To quit to main menu')
		num = input()
		if num == '1':
			num1=login(name, password)
			print(num1)
			return num1
		elif num == '2':
			num1=re_enter_details()
			print(num1)
			return num1
		else: 
			return '0'


	
def login(name, password):
	"""
	Evaluates if the password and 
	corresponding name exist in the accounts dictionary
	with option of adding new account & reentering password
	param: name & password
	return: n/a
	"""
	
	if name in accounts.values():
		if password in accounts.keys():
			if name==accounts.get(password):
				#if name is value whose key is password
				current_clientname.clear()
				current_clientname.append(name)
				print(current_clientname[0])#s
				print("Hello {0}!\nYou are logged in".format(name))
				return '1'
		
		else:
			print("\nInvalid password")
			num = input("Press\n1. To Re enter only Password\n2. To Re enter all details\n3. To quit to Main menu\n")
			if num=='1':
				#re enter only password
				password1=input("Enter password: ")
				num1 =login(name,password1)
				print(num1)
				return num1
			elif num=='2':
				#reenter all details
				num1 =re_enter_details()
				print(num1)
				return num1
			else:
				#quit application
				print('Ts NOT OK to give up!')
				print('------------------------------------------------------------------------------------------------------\n')
				return 0
				
	else:
		print("\nInvalid username or password")
		print("Press\n1. To Create a new account\n2. To Retry\n3.(or any other character) To quit\n")
		num = input()
		print(num)
		if num=='1':
			num1=add_account(name,password)
			print('------------------------------------------------------------------------------------------------------\n')
			print(num1)
			return num1
		elif num=='2':
			num1=re_enter_details()
			print('------------------------------------------------------------------------------------------------------\n')
			print(num1)
			return num1
		else:
			print('------------------------------------------------------------------------------------------------------\n')
			return 0

def re_enter_details():
	"""
	re enter your username and password
	param: n/a
	return: n/a
	"""
	name1=input('Enter username: ')
	password1=input('Enter password: ')
	num1 =login(name1,password1)
	return num1

def add_info_to_all_client_todos(name):
	"""
	Adds client todo list to list with all clients' todos
	param: name of client
	return: n/a
	"""
	#print(todo_list)
	client_todos[name]= []
	# if todo_list is not empty:
	# 	del todo_list[:]#empty todo_list
	#todo_list=client_todos.get(name)
	#print(todo_list)#

def save_client_info(todolist):
	client_todos[current_clientname[0]]=todolist
	print(client_todos)
	print(current_clientname)
	print(client_todos[current_clientname[0]])