class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        answer = 0 #initialize variable
        for i in range(len(points) - 1): #for every set of points, a loop
            mov_x, mov_y = points[i]  #set the current points as location 
            target_x, target_y = points[i + 1] #set the next points as the target
            answer += max(abs(target_x - mov_x), abs(target_y - mov_y)) #calculate shortest possible path using the maximum difference between current and target in both X and Y axis, add it to total answer in int.
            
            
            
        return answer