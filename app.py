#This file contains the entry point to your tasks 
#adn the logic to manage it

from tasks import *
#import other functions as well

from accounts import *
#imports the function 


#def
def manipulate_todo_list():
	'''manipulate todo list
	param: n/a
	return: n/a
	'''
	print('\nEnter')
	print("1. To View To Do List")
	print("2. To Create a Task")
	print("3. To Mark a Task as Finished")
	print("4. To Delete a Task")
	print("5. To Delete All Tasks")
	print("6. Leave App")
	num=raw_input()

	if num=='1':
		#view all tasks
		if todo_list != []:
			a=1
			for todo in todo_list:
				print('{0} {1}'.format(a,todo))
				a+=1
			manipulate_todo_list()
		
		else:
			print('No Tasks at the moment')
			print('Please add more tasks to your todo list')
			manipulate_todo_list()
	elif num=='2':#add tasks
		add_tasks()

	elif num=='3':#mark as finished
		mark_finished_task()

	elif num=='4':#delete a task
		deletes_task()

	elif num=='5':#delete all tasks
		print('Are You sure you want to delete all your tasks')
		print('Press')
		print('Y for yes')
		print('Any other character for no')
		decision=raw_input()
		if decision=='y':
			delete_all_tasks()
			manipulate_todo_list()
		else:
			manipulate_todo_list()

def add_tasks():
	"""
	This function adds tasks to ToDo List
	param: n/a
	return: n/a
	"""
	task=raw_input('Enter Task to Add:')
	create_task(task)
	print('\nEnter')
	print('1. To Add another task')
	print('2.(Or any other no) To Go to main menu')
	num=raw_input()
	if num=='1':
		add_tasks()
	else:
		manipulate_todo_list()

def mark_finished_task():
	"""
	This function Marks tasks as finished
	param: n/a
	return: n/a
	"""
	task_to_mark=(check_todolist())
	if(type(task_to_mark)==int):
		# if user input is an integer
		#delete the selected task
		if task_to_mark<=(len(todo_list)) and task_to_mark>0: 
			mark_as_finished(todo_list[task_to_mark-1])
			manipulate_todo_list()
		else:
			#if integer is not listed
			print('Your input is invalid')
			mark_finished_task()
	elif task_to_kill=='Add tasks to your to do list':
		#if todo list is empty
		print(task_to_mark)
		manipulate_todo_list()
	else:
		#if user inputs unnecessary data
		print('Your input is invalid')
		mark_finished_task()
	


def deletes_task():
	"""
	This function deletes selected task
	param: n/a
	return: n/a
	"""
	task_to_kill=(check_todolist())
	if(type(task_to_kill)==int):
		# if user input is an integer
		#delete the selected task
		if task_to_kill<=(len(todo_list)) and task_to_kill>0: 
			delete_task(todo_list[task_to_kill-1])
			manipulate_todo_list()
		else:
			#if integer is not listed
			print('Your input is invalid')
			deletes_task()
	elif task_to_kill=='Add tasks to your to do list':
		#if todo listis empty
		print(task_to_kill)
		manipulate_todo_list()
	else:
		#if user inputs unnecessary data
		print('Your input is invalid')
		deletes_task()

def check_todolist():
	'''
	Displays todo list and allows user to enter the number of the
	task to be manipulated
	params: n/a
	returns: index of 
	'''
	if len(todo_list)!=0:
		#if todo list is not empty
		i=1
		dictionary={}

		print('Your To Do List')
		for todo in todo_list:
			dictionary[i]=todo
			print("{0}.  {1}".format(i,todo))
			i+=1
		
		print("Enter the number of the todo list you would like to manipulate")
		num=raw_input()
		index=int(num)
		return index

	else:
		#if todo list is empty
		print('Your to do list is empty')
		return 'Add tasks to your to do list'

def start_application():
	print("Press")
	print("1. To Log in To Your account")
	print("2. To Sign Up/Create a new Account")
	print("3. or any other character to bounce")
	num= raw_input()
	if num=='1':
		#login
		name=raw_input('Enter your username: ')
		password= raw_input('Enter your password: ')
		
		num1=login(name,password)
		if num1=='1':
			manipulate_todo_list()
		
	elif num=='2':
		#signup
		name=raw_input('Enter your desired username: ')
		password= raw_input('Enter your desired password: ')
		num1=add_account(name,password)
		if num1=='1':
			manipulate_todo_list()
	else:
		#if u goin bounce
		print("---------OUT!!---------")


if __name__=="__main__":
	start_application()
	#Allow person to input name and password
	#
	#let person sign in. 
	#if details do not exist create account for them
	#allow user to manipulate to do list, that is, 
	#add task
	#mark task as finished
	#delete task, 
	
	"""provide options
		>create a task
		>delete a task
		>delete all tasks
		>mark a task as finished

		e.g
		print("select option:")
		print("1: Create Task")
		....skipped code
		selection = input("selection: ")
		write code that implements the selected option
	"""

# def enter_details():
# 	name=raw_input('Enter your username: ')
# 	password= raw_input('Enter your password: ')

# 	return name,password

