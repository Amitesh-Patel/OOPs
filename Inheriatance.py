class Employee:
	raise_amount = 1.04   
	no_of_emp = 0  
	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay

		Employee.no_of_emp+=1   

	def fullname(self):
		return f"{self.first}{self.last}"

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

class Developers(Employee): #inherit from employee class
	raise_amount = 1.10
	def __init__(self,first,last,pay,proglang):
		super().__init__(first, last,pay)  #this argumnets will be passed to employee class and that class will handle all thier methods
		self.proglang = proglang

class Manager(Employee):

	def __init__(self,first,last,pay,employee = None):    #why didnt the default empty list . We should not pass mutable datatype as argument 
		super().__init__(first, last,pay) 
		if employee is None:
			self.employee = []
		else:
			self.employee=employee

	def add_emp(self,emp):
		if emp not in self.employee:
			self.employee.append(emp)

	def remove_emp(self,emp):
		if emp  in self.employee:
			self.employee.remove(emp)

	def print_emp(self):
		for emp in self.employee:
			print('-->',emp.first)

dev_1 = Developers('Amitesh','patel',300000 , 'python')
dev_2 = Developers('Sudip','mandal',400000,'java')

# print(dev_1.proglang)

mgr_1 = Manager('Sue','Smith',90000,[dev_1])
print(mgr_1.print_emp())

mgr_1.add_emp(dev_2) 
print(mgr_1.print_emp())