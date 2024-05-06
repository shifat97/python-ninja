# O(2n) solution 
def findSecondLargest(arr):
  max = 0
  for number in arr:
    if number > max:
      max = number

  second_max = 0
  for number in arr:
    if number > second_max and number < max:
      second_max = number

  return second_max

# O(n) solution
def secondLargest(arr):
  max = arr[0]
  second_max = -1

  for number in arr:
    if number > max:
      second_max = max 
      max = number
    elif number < max and number > second_max:
      second_max = number
  
  return second_max

arr = [3, 2, 1, 5, 2, 4]
ans = findSecondLargest(arr)
print(f'Largest is {ans}')
ans2 = secondLargest(arr)
print(f'Second Largest is: {ans2}')