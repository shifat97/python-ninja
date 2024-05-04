def reverseArray(arr, n):
  ans = []
  i = n - 1
  while i >= 0:
    ans.append(arr[i])
    i = i - 1

  return ans


arr = [ 4, 3, 20, 4, 1, 2, 0, 10 ]
n = len(arr)
res = reverseArray(arr, n)
print(f'Reversed {res}')