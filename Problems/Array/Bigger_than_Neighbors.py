def findPeak(arr, n):
  ans = []
  if n == 1:
    ans.append(arr[0])
  if arr[0] >= arr[1]:
    ans.append(arr[0])
  if arr[n-1] >= arr[n-2]:
    ans.append(arr[n-1])
  
  for i in range(1, n - 1):
    if(arr[i] >= arr[i-1] and arr[i] >= arr[i+1]):
      ans.append(arr[i])

  return ans;

arr = [ 4, 3, 20, 4, 1, 2, 0, 10 ]
n = len(arr)
res = findPeak(arr, n)
print(f'Peak elements are {res}')