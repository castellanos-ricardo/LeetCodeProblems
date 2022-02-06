class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        exclusiveOR = bin(x ^ y)[2:]
        return sum([int(x) for x in exclusiveOR])
        