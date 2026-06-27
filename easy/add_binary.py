class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
            """

        i=len(a)-1
        j=len(b)-1
        final=[]
        carry=0

        while i >= 0 or j >= 0 or carry > 0:

            num_a =int(a[i]) if i>=0 else 0
            num_b =int(b[j]) if j>=0 else 0
                       

            sum=num_a+num_b+ carry
            
            actual_number=sum%2
            
            carry=sum//2
            
            final.append(str(actual_number))

            i-=1
            j-=1

        return "".join(final[::-1])

