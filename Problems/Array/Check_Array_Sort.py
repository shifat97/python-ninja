def checkSorted(arr):
  for i in range(1, len(arr)):
    if arr[i] >= arr[i-1]:
      continue
    else:
      return False

  return True

arr = [1, 1, 2, 2, 2, 3, 4, 5, 4]
ans = checkSorted(arr)
if ans:
  print('Sorted')
else:
  print('Not Sorted')