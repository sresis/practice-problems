class Solution:
    def generateTheString(self, n: int) -> str:
        output = ''
        if n % 2 == 0:
            output = 'a' * (n-1)
            output += 'b'
            return output
        else:
            output = 'a' * n
            return output
            
        