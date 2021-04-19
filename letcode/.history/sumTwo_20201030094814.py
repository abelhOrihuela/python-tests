class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        print("Target => ", target)
        print("Nums => ", nums)


        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]



solution = Solution()

# result = solution.twoSum([2, 7, 11, 15], 9)
result = solution.twoSum([3, 2, 4], 6)
# result = solution.twoSum([3, 3], 6)


print(result)