def selectionSort(arr, n):
  for i in range(0, n-1):
    index_min = i
    for j in range(i+1, n):
      if arr[j] < arr[index_min]:
        index_min = j
    
    if index_min != i:
      temp = arr[i]
      arr[i] = arr[index_min]
      arr[index_min] = temp

  return arr


arr = [10, 2, 5, 8, 7]
n = len(arr)
res = selectionSort(arr, n)
print(f'Sorted {res}')