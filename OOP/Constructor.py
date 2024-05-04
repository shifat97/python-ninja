class Student:
  def __init__(self, name, country, nationality):
    self.name = name
    self.country = country
    self.nationality = nationality

  def displayStudent(self):
    print(self.name)
    print(self.country)
    print(self.nationality)
    print('\n')

s1 = Student('Bin Laden', 'Canada', 'Canadian')
s2 = Student('Donal Trump', 'United States', 'USA')
s3 = Student('Joe Biden', 'India', 'Indian')

s1.displayStudent()
s2.displayStudent()
s3.displayStudent()

class Developer:
  def __init__(self, name, stack, experience):
    self.name = name
    self.stack = stack
    self. experience = experience

  def displayDeveloper(self):
    print(f'Name: {self.name}, Stack: {self.stack}, Experience: {self.experience} years')

dev1 = Developer('John Doe', 'Django', 1)
dev2 = Developer('Bruce Lee', 'Spring Boot', 3)
dev3 = Developer('Tony Stark', 'NodeJS', 5)

dev1.displayDeveloper()
dev2.displayDeveloper()
dev3.displayDeveloper()
