# Brute force
def containsDuplicate(nums):
  for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
      if nums[i] == nums[j]:
        return True
  return False

# Optimize solution
def optimized(nums):
  seen = set()
  for num in nums:
    if num in seen:
      return True
    seen.add(num)
  return False

nums = [1, 2, 3, 1]
res = containsDuplicate(nums)
print(res)
res2 = optimized(nums)
print(res2)