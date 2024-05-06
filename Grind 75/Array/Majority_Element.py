def majorityElement(nums):
  count = 0
  item = 0
  for num in nums:
    if count == 0:
      item = num
    if num == item:
      count += 1
    else:
      count -= 1
  return item

nums = [3, 2, 3]
res = majorityElement(nums)
print(res)