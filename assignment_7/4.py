class Pair:
  def twoSum(self, nums, target):
      a = {}
      for i, num in enumerate(nums):
          if target - num in a:
               return (a[target - num], i)
          a[num] = i


num = [10, 20, 10, 40, 50, 60, 70]
target=50
print("%d,%d" % Pair().twoSum(num,target))
