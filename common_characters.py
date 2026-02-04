from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])

        for word in words[1:]:
            common &= Counter(word)

        output = []

        for char, freq in common.items():
            output.extend([char] * freq)

        return output
