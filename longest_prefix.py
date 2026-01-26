class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        for i, char in enumerate(strs[0]):
            for word in strs:
                if i >= len(word) or  word[i] != char:
                    return output

            output += char

        return output
