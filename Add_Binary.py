class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def decimalToBinary(n):
            return bin(n).replace("0b", "")
        a = int(a,2)
        b = int(b,2)
        bi = decimalToBinary(a+b)
        return str(bi)
