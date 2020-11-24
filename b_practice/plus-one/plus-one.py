class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        #convert to string then int
        num = ''
        for item in digits:
            num += str(item)
        
        carry = 1
        array = []
        for i in range(len(num)-1, -1, -1):
            current_sum = carry + int(num[i])
            array.append(current_sum % 10)
            carry  = current_sum // 10
        # handle leftover
        if carry != 0:
            array.append(carry)
        array = array[::-1]
        return array