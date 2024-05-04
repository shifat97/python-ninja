def twoSum(nums, target):
  unique = {}
  i = 0
  while i < len(nums):
    complement = target - nums[i]
    if complement in unique:
        return [unique[complement], i]
    unique[nums[i]] = i
    i = i + 1  

  return []

result = twoSum([2,7,11,15], 9)
print(result)