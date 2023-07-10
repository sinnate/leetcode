class Solution:
    def isValid(self, s: str) -> bool:
        chunk = []
        for char in s :
            if char == 'c':
                if len(chunk) < 2 or chunk[-2] != 'a' or chunk[-1] != 'b':
                    return False
                chunk.pop()
            else:
                chunk.append(char)
        return not chunk