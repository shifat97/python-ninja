# O(nLogn) solution
def sortArray(arr):
  arr.sort()
  n = len(arr)
  return arr[n - 1]


# O(n) solution 
def findLargest(arr):
  large = 0
  for number in arr:
    if number > large:
      large = number
  return large

arr = [3, 2, 1, 5, 2]

res = findLargest(arr)
print(f'Largest is {res}')

res2 = sortArray(arr)
print(f'Largest is {res2}')