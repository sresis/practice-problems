class Solution:
    def removeDuplicates(self, S: str) -> str:
        # use a stack here
        # only need to remove 2 duplicates in a row
        stack = []
        new_str = ''
        for i in range(len(S)):
            if stack == []:
                stack.append(S[i])
                new_str += S[i]
                
            elif S[i] == stack[-1]:
                new_str = new_str[:-1]
                stack.pop()
            else:
                new_str += S[i]
                stack.append(S[i])
        return new_str