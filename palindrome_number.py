class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        intToStr = str(x)

        for i in range(len(intToStr)):
            if intToStr[i] != intToStr[len(intToStr) - i -1]:
                return False
        return True


s = Solution()

print(s.isPalindrome(-123))