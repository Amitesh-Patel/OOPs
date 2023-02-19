#python object oriented programming


#how to create a class
class Employee:
	def __init__(self,first,last,email):
		self.first = first
		self.last = last
		self.email = email
	def fullname(self):
		return f"{self.first}+{self.last}"



emp1 = Employee('Amitesh','patel','aa@gmail.com')
print(emp1.fullname())