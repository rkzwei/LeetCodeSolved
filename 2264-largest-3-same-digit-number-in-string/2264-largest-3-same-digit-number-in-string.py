class Solution:
    def largestGoodInteger(self, num: str) -> str:
        answer = -1 #initialize our answer
        for i in range(len(num)-2): #since we are checking for substrings of 3, we start 2 under
            if num[i] == num[i + 1] == num[i + 2]: #comparative check to see they're the same
                answer = max(answer, int(num[i])) #we have no need for the extra numbers, so we check between what we got and the current evaluation
        return "" if answer == -1 else str(answer) * 3 #simple return if we never got a valid substring, or three times the biggest int we found as st