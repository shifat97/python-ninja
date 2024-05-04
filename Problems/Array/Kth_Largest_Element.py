def kthLargest(arr, n, k):
  for i in range(1, n):
    item = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > item:
      arr[j+1] = arr[j]
      j = j - 1
    
    arr[j+1] = item
  
  return arr[k - 1]

arr = [10, 2, 5, 8, 7]
n = len(arr)
k = 3
res = kthLargest(arr, n, k)
print(f'Sorted {res}')