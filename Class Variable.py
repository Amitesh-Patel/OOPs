#python object oriented programming



class Employee:

	#a class variable
	raise_amount = 1.04   # we cannot change the variable for every employee we want differnt raise amount for evry employee
	no_of_emp = 0   #this is the variable that we want to change whenever applied not for single instance

	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay

		Employee.no_of_emp+=1   #for every instance it changes 

	def fullname(self):
		return f"{self.first}{self.last}"

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)



emp1 = Employee('Amitesh','patel',50000)

emp2 = Employee('Amit','patel',60000)

Employee.raise_amount = 1.05   #changes the raise amount for all the instance
emp1.raise_amount = 1.06   #changes the raise amount for only emp1 instance

print(Employee.raise_amount)   #we can see the variable with the help of class

print(emp1.raise_amount)
print(emp2.raise_amount)       #also we can see the variable with th ehelp of instance

print(emp1.__dict__)

print(Employee.__dict__)


print(emp1.no_of_emp)