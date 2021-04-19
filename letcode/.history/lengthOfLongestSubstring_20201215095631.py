class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlength = 0
        dicts = {}

        for i, value in enumerate(s):
            if value in dicts:
                sum = dicts[value] + 1

                print(sum)
                maxlength+=1

        print(dicts)
        print(maxlength)

        return maxlength        

solution = Solution()

solution.lengthOfLongestSubstring("pwwkew")