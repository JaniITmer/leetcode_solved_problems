class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

    
    if n<=2:
        return n
    a=1
    b=2
    for i in range(3,n+1):
        next=a+b
        a=b
        b=next

    return b

    
