class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # create a window that decreases its length from the right
        # left side of the window is used to match the letter and the right side is used
        # to reduce the window length
        left = 0
        right = len(strs) - 1
        curSolution = strs[0]
        for item in strs[1:]:
            while left < len(item) and left < len(curSolution) and item[left] == curSolution[left]:
                left += 1
            
            right = left
            left = 0
            curSolution = curSolution[left:right]
            print(curSolution)
        return curSolution