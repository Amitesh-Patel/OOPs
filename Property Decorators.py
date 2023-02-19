#property decorators are used to set methods that can be used as attributes
#they didnt require any parenthesis if you updated that code other user of that class can still use as it is.



class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property         #setting the property decorators
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter       
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('Amit', 'Patel')
emp_1.fullname = "Amitesh PAtel"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname