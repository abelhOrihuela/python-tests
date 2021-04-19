class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlength = 0
        dicts = {}

        for i, value in enumerate(s):
            if not value in dicts:
                dicts[value] = i
                maxlength+=1

        print(maxlength)
        print(dicts)
        

solution = Solution()

solution.lengthOfLongestSubstring("HOOOOOOLA")