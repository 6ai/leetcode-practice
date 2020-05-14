# 190. Reverse Bits

class Solution:
    def reverseBits(self, n: int) -> int:
        bin_num = format(n, 'b')
        res = '0' * (32-len(bin_num)) + bin_num
        return int('0b' + res[::-1], 2)
