class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal) : return False
        elif s == goal : 
            setS = list(set(list(s)))
            if len(setS) < len(s) : return True
            else : return False
        
        diff = []
        for i in range(len(s)) :
            if s[i] != goal[i] : 
                if len(diff) == 2 : return False
                else : diff.append(i)
        
        if len(diff) < 2 : return False
        listS = list(s)
        temp = listS[diff[0]]
        listS[diff[0]] = listS[diff[1]]
        listS[diff[1]] = temp
        return ''.join(listS) == goal