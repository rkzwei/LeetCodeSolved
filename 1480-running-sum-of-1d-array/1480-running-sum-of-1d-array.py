class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = [nums[0]] #start at 0th running sum, since we don't sum it to anything
        for i in range (1, len(nums)): #loop starting at 1, since 0 already accounted, max range lenght of array nums
            answer.append(answer[i-1]+nums[i]) 
            #add to answer array -> the current answer index in nums - 1, to add the last entry, then add current nums index together. 
        #This makes a new sum that correctly incorporates everything before, while moving forward.
        #With this format, the code answers at execution.
           
        return answer