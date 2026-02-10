class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        transformations = set()

        for word in words:
            code = "".join(morse_code[ord(char) - ord('a')] for char in word)
            transformations.add(code)

        return len(transformations)
        
        
        
        # brute force
        # morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        # alphabets = list("abcdefghijklmnopqrstuvwxyz")
        # output = {}
        # for word in words:
        #     code = ""
        #     for char in word:
        #         code += morse_code[alphabets.index(char)]
            
        #     if code in output:
        #         output[code] += 1
            
        #     output[code] = 1

        # return len(output)
                
            
            
        
