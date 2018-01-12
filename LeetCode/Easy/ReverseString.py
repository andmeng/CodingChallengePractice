class Solution:
    # Recursive solution
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        else:
            return s[-1:] + self.reverseString(s[0 : len(s) - 1])


solutionObject = Solution()

sampleString = "apple"

print(solutionObject.reverseString(sampleString))