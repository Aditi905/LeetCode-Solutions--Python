class Solution:
    def judgeCircle(self, moves: str) -> bool:
        up=0
        right=0
        down=0
        left=0
        for i in moves:
            if i=='U':
                up+=1
            elif i=='D':
                down+=1
            elif i=='L':
                left+=1
            else:
                right+=1
        if up==down and right==left:
            return True
        else:
            return False
        