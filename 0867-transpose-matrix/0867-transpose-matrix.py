#objective is to transpose the matrix, which can be accomplished by looping the length of both lists given and recomposing the lists that comprise the matrix. 

#luckily python has a built-in solution for this, so we actually only need one function call for zip.

#zip will iterate through the shortest length only, but since our matrix is a linked list, it'll always work for our intended purpose.
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return zip(*matrix)