class Solution:
    def main(self, s: str) -> int:
        previousChars = ''
        answer = 0
        for char in s:
            if char in previousChars:
                answer = len(previousChars) if len(
                    previousChars) > answer else answer
                previousChars = char
                continue
            previousChars += char
        return answer
