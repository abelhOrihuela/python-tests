class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        for i, value in enumerate(s):
            print(i, value)
        

solution = Solution()

solution.lengthOfLongestSubstring("HOOOOOOLA")