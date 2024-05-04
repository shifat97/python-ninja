def rotate(arr, n):
  last_element = arr[n-1]
  i = n - 2
  while i >= 0:
    arr[i+1] = arr[i]
    i = i - 1
  arr[0] = last_element
  return arr

arr = [2, 3, 4, 5, 1]
n = len(arr)
res = rotate(arr, n)
print(f'Rotated: {res}')
