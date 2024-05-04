def findIntersection(arr1, arr2, n1, n2):
  ans = []
  for i in range(n1):
    for j in range(n2):
      if arr1[i] == arr2[j]:
        ans.append(arr1[i])

  return ans

arr1 = [1, 3, 4, 5, 7]
arr2 = [2, 3, 5, 6]
n1 = len(arr1)
n2 = len(arr2)
res = findIntersection(arr1, arr2, n1, n2)
print(res)
