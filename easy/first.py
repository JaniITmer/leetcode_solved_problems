
class Solution(object):
    def removeDuplicates(self, nums):
        writer=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[writer]=nums[i]
                writer+=1
                
        return writer



input=[1,1,2]
megoldas=Solution()
print(megoldas.removeDuplicates(input))

    
        
        
