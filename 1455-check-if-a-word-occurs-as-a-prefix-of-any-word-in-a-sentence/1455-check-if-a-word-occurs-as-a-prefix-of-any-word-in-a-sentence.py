class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        list_sentence = sentence.split(' ')
        
        for i in range(len(list_sentence)):
            if searchWord in list_sentence[i]:
                for j in range(len(list_sentence[i])):
                    if list_sentence[i][:j + 1] == searchWord:
                        return i + 1
        
        return -1
        
        