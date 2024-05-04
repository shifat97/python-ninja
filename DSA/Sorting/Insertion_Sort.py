def insertionSort(arr, n):
  for i in range(1, n):
    item = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > item:
      arr[j+1] = arr[j]
      j = j - 1
    
    arr[j+1] = item
  
  return arr

arr = [10, 2, 5, 8, 7]
n = len(arr)
res = insertionSort(arr, n)
print(f'Sorted {res}')