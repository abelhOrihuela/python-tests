class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlength = 0
        dicts = {}

        for i, value in enumerate(s):
            print(i, value)

            if not value in dicts:
                dicts[value] = 1
                maxlength+=1

        print(dicts)
        

solution = Solution()

solution.lengthOfLongestSubstring("HOOOOOOLA")