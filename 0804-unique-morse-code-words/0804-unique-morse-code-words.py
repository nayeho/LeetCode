class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        dic_word = {'a' : '.-', 'b' : '-...', 'c' : '-.-.', 'd' : '-..', 'e' : '.',
         'f' : '..-.', 'g' : '--.', 'h' : '....', 'i' : '..', 'j' : '.---',
         'k' : '-.-', 'l' : '.-..', 'm' : '--', 'n' : '-.', 'o' : '---',
         'p' : '.--.', 'q' : '--.-', 'r' : '.-.', 's' : '...', 't' : '-',
         'u' : '..-', 'v' : '...-', 'w' : '.--', 'x' : '-..-', 'y' : '-.--',
         'z' : '--..'}
        
        words_list = []
        
        for word in words:
            length = len(word)
            morse = ''
            for i in range(length):
                morse += dic_word[word[i]]
                
            words_list.append(morse)
            
        words_set = set(words_list)
        
        return len(words_set)
        
        