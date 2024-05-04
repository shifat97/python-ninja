def bubbleSort(arr, n):
  for i in range(0, n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp

  return arr

arr = [10, 2, 5, 8, 7]
n = len(arr)
res = bubbleSort(arr, n)
print(f'Sorted {res}')