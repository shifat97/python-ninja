def findSecondSmallest(arr):
  min = arr[0]
  second_min = 2147483647

  for number in arr:
    if number < min:
      second_min = min
      min = number
    elif number < second_min and number > min:
      second_min = number
  
  return second_min

arr = [3, 1, 2, 5, 4, 2]
ans = findSecondSmallest(arr)
print(f'Smallest is: {ans}')


# min = 2147483647

#   for number in arr:
#     if number < min:
#       min = number

#   second_min = 2147483647

#   for number in arr:
#     if number < second_min and number > min:
#       second_min = number