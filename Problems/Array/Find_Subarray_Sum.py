def subArraySum(arr, sum, n):
  for i in range(n):
    currentSum = arr[i]
    if currentSum == sum:
      print(f'Sum found at index {i}')
      break
    else:
      for j in range(i+1, n):
        currentSum += arr[j]
        if currentSum == sum:
          print(f'Sum found in between {i} to {j}')
          break

arr = [1, 4, 20, 3, 10, 5, 33]
sum = 33
n = len(arr)
res = subArraySum(arr, sum, n)