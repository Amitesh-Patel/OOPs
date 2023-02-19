#python object oriented programming

#class Method - automatically pass cls as first argument 
#regular method - automatically pass instance self as first argument
#static method - doesnot pass automatically anything they dont pass instance or class
class Employee:

	#a class variable
	raise_amount = 1.04   
	no_of_emp = 0  
	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay

		Employee.no_of_emp+=1   #for every instance it changes 

	def fullname(self):
		return f"{self.first}{self.last}"

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	@classmethod
	def set_raise_amt(cls,amount):
		cls.raise_amount=amount

	@classmethod
	def from_string(cls,string):
		first,last,pay = string.split('-')
		return cls(first,last,pay)   #here we used cls to create object


	#when to use static method , you can use static method when either class or self methods are not
	#used in the method in above example cls is used but in down ex no class or self is required so use static
	@staticmethod
	def is_work(day):
		if day.weekday() == 5 or day.weekday() == 6:    
			return False
		return True



#For class Method
# emp1 = Employee('Amitesh','patel',50000)

# emp2 = Employee('Amit','patel',60000)
# Employee.set_raise_amt(1.05)

# new_emp = Employee.from_string('Amitesh-Patel-20000')
# print(new_emp.first)


# print(Employee.raise_amount)   #we can see the variable with the help of class

# print(emp1.raise_amount)

#for static method
import datetime
my_data = datetime.date(2016,7,10)

print(Employee.is_work(my_data))

