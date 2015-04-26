import sys
import os
import json

TODO_FILENAME = os.path.join(os.getcwd(), '.todo.list')

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	RECV = '\033[33m' # yellow
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	INFO = '\033[37m'
	WHITE = '\033[97m'

class Status:
	PENDING = "PENDING"
	DONE = " DONE"

class Todo:
	'''One Todo
	'''
	def __init__(self, content, status=Status.PENDING, prior=5):
		self.content = content

	def complete():
		self.status = Status.DONE

	def undo():
		self.status = Status.PENDING

	def lower(i=1):
		if(self.prior >= 0 or self.prior <=10):
			self.prior--

	def upper(i=1):
		if(self.prior >= 0 or self.prior <=10):
			self.prior++

class TodoManager:
	'''Use to manage todo-list and file.
	'''
	todoList = {}
	def __init__(self):
		with open(TODO_FILENAME, 'r') as f:
			todoList = json.load(f)

	def newTodo(self,content):
		tid = len(open(TODO_FILENAME, 'r').readlines()) + 1
		Todo todo(content)
		todoList[tid] = todo
		with open(TODO_FILENAME, 'w') as f:
			json.dump(todoList, f)
