class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        biggest_val = 0
        second_biggest_val = 0 #initialize 2 variables, so we can run through the array while storing the values
        for num in nums:
            if num > biggest_val: #if current value is larger than stored biggest, hand over to second and store biggest
                second_biggest_val = biggest_val
                biggest_val = num
            else: #compare current to the max of second biggest and current to see if store.
                second_biggest_val = max(second_biggest_val, num)
        
        return (biggest_val - 1) * (second_biggest_val - 1)
    
    