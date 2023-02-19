#special methods are used to change some builtin behaviours like when we print any object it will print something
#which is not user friendly . Ex - they are basically in double underscore __init__ , __repr__ , __str__
#are called dunders

class Employee:

	raise_amount = 1.04  

	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay

	def fullname(self):
		return f"{self.first}{self.last}"

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	def __repr__(self):
		return "Employee(f'{self.first} , {self.last} , {self.pay}')"

	def __str__(self):
		return '{} - {}'.format(self.first,self.last)

	def __add__(self,other):
		return self.pay + other.pay

	def __len__(self):
		return len(self.first)

emp1 = Employee('Amitesh','patel',20000)
emp2 = Employee('Amit','patel',30000)

print(emp1)
repr(emp1)
# str(emp1)
# print(add(emp1,emp2))
print(len(emp1))




