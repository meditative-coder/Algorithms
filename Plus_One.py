class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(i) for i in digits]
        digits = int("".join(digits))
        digits = digits + 1
        results = list()
        while(digits):
            results.append(digits%10)
            digits = digits//10
        results.reverse()
        return results
            
        # lent = len(digits)
        # carry = 0
        # for i in range(lent-1,-1,-1):
        #     if i==lent-1:
        #         digits[i] = digits[i]+1
        #     else:
        #         digits[i] = carry+digits[i]
        #         carry = 0
        #     if digits[i]>9:
        #         carry = digits[i]-9
        #         digits[i] = digits[i]-10
        #     if carry == 0:
        #         break
        # if carry!=0:
        #     return [carry]+digits
        # return digits
