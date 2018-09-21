#This file manages the todo list
todo_list =[]


def create_task(task):
	#adds task(string value)  to your todo list
	#param:
	#return:
	todo_list.append(task)
	for i in todo_list:
		print(i)


def delete_task(task):
	#removes specified task from the todo list
	#param:
	#return:
	todo_list.remove(task)


def mark_as_finished(task):
	#Append the string label '[finished]' at the end of the task
	#if it does not already have the label appended
	#Should remain in the todo list
	#param:
	#return:
	if(task in todo_list):
		if(task.endswith('[finished]')):
			print('Task already marked as complete')
		else:
			todo_list.remove(task)
			task += '[finished]'
			todo_list.append(task)
			print('{0} {1}'.format('Marked', task))





def delete_all_tasks():
	#Empties todo_list
	#param:n/a
	#return:n/a
	del todo_list[:]
	print('To Do List has been emptied') 
	print('All your tasks are caput')

# create_task("Go to barber's")

# create_task("Go to Court")
# print(todo_list)
# delete_task("Go to Court")
# mark_as_finished("Go to Court")
# print (todo_list)

