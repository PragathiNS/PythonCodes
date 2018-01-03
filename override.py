class Employee(object):
  def __init__(self, name):
    self.name = name
  def greet(self, other):
    print "Hello, %s" % other.name
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

class CEO(Employee):
  def greet(self, other):
    print "Get back to work, %s!" % other.name

class PartTimeEmployee(Employee):
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00
    
  def full_time_wage(self, hours):
    return super(PartTimeEmployee, self).calculate_wage(hours)
    
ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo)
# Hello, Emily
ceo.greet(emp)
# Get back to work, Steve!

pte = PartTimeEmployee("PT_Josh")
print pte.calculate_wage(3)
# 36.0
print emp.calculate_wage(3)
# 60.0

milton = PartTimeEmployee('milton')
print milton.full_time_wage(10)
# 200.0
