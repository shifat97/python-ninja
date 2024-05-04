message = '''
Hi John,
    
Here is our first email to you.
    
Thank you,
The support team
'''

print(message)
course = 'Python for Beginners'
print(course[0])
print(course[-1])
print(course[0:6])
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('P'))
print(course.split(' '))
new_course = course.replace('Python', 'Java')
print(new_course)
print('Python' in course)
print(course.title())

first = 'John'
last = 'Smith'
print(f'{first} {last} is a programmer.')
