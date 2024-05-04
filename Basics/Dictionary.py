num_to_words = dict()

num_to_words[1] = 'One'
num_to_words[2] = 'Two'
num_to_words[3] = 'Three'

print(num_to_words)
print(num_to_words[3])

if 2 in num_to_words:
  print('Available')
else:
  print('Not found')

for item in num_to_words:
  print(item, num_to_words[item])

print(num_to_words.get(1))
print(num_to_words.get(5))

li = [(1, 'One'), (2, 'Two'), (3, 'Three')]
dt = {k:v for k, v in li}
print(dt)
dt2 = {v:k for k, v in li}
print(dt2)