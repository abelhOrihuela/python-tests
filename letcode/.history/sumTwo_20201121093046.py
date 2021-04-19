class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        print("initial data")
        print(nums)
        print(target)
        h = {}

        for i, num in enumerate(nums):
            print("index", i)
            print("num", num)
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]



solution = Solution()

# result = solution.twoSum([2, 7, 11, 15], 9)
result = solution.twoSum([3, 2, 4, 6, 2, 9], 15)
# result = solution.twoSum([3, 3], 6)


print(result)