# 172. Factorial Trailing Zeroes
# Medium
# Topics
# Companies

# Given an integer n, return the number of trailing zeroes in n!.

# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # the number of times 5 in mulitplied is the number of zeros.............
        result = 0
        
        while n > 0:
            n = n // 5
            result += n
            
        return result
    
    
solution = Solution()

print(solution.trailingZeroes(25))