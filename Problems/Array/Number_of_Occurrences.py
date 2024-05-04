def findOccurrence(arr, x, n):
  count = 0
  for i in range(n):
    if arr[i] == x:
      count = count + 1
  
  return count

arr = [1, 1, 2, 2, 2, 2, 3]
x = 2
n = len(arr)
res = findOccurrence(arr, x, n)
print(f'Number of occurrences: {res}')