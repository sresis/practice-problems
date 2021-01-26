class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod_dig = 1
        sum_dig = 0
        n = str(n)
        for i in range(len(n)):
            prod_dig *= int(n[i])
            sum_dig += int(n[i])
        return prod_dig - sum_dig
        
        