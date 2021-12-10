from math import factorial
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            temp = []
            for j in range(i+1):
                temp.append(factorial(i)//(factorial(j)*factorial(i-j)))
            result.append(temp)
        return result
