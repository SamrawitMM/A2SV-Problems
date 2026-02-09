class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set("qwertyuiop")
        second_row = set("asdfghjkl")
        third_row = set("zxcvbnm")

        output = []
        for word in words:
            word_lower = word.lower()
            if set(word_lower).issubset(first_row) or set(word_lower).issubset(second_row) or set(word_lower).issubset(third_row):
                output.append(word)
        
        return output

