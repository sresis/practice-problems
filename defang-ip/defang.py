class Solution:
    def defangIPaddr(self, address: str) -> str:
        # go through each char
        # if it is .
        # new_str = new_str[:i] + '[.]'
        new_str = ''
        for i in range(len(address)):
            if address[i] == '.':
                new_str = new_str + '[.]'
            else:
                new_str += address[i]
        return new_str