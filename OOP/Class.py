class Employee:
  def __init__(self, id, name):
    self.id = id
    self.name = name
  
  def display(self):
    print(self.id, ':', self.name)

emp1 = Employee(101, 'John Doe')
emp1.display()
emp2 = Employee(102, 'Donald Trump')
emp2.display()