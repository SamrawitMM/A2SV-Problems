class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        reverse = []
        q = x // 10
        r = x % 10
        reverse.append(r)
        while q  != 0:
            r = q % 10
            q  = q // 10
            reverse.append(r)

        return x == int("".join(map(str, reverse)))
