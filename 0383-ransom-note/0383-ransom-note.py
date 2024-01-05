class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        list_reansomNote = list(ransomNote)
        list_magazine = list(magazine)
        unique_list_reansomNote = list(set(list_reansomNote))
        
        for word in unique_list_reansomNote:
            cnt_reansomNote = list_reansomNote.count(word)
            cnt_magazine = list_magazine.count(word)
            if cnt_reansomNote <= cnt_magazine:
                pass
            else:
                return False
        
        return True
        