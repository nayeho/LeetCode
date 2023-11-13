class Solution:
    def sortVowels(self, s: str) -> str:
        kVowels = 'aeiouAEIOU'
        answer = []
        vowels = sorted([c for c in s if c in kVowels])

        i = 0  # vowels' index
        for c in s:
            if c in kVowels:
                answer.append(vowels[i])
                i += 1
            else:
                answer.append(c)

        return ''.join(answer)