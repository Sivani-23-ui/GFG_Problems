class Solution:
    def pairAndSum(self, arr):
        total = 0
        for bit in range(32):
            cnt = sum(1 for x in arr if (x >> bit) & 1)
            total += (cnt * (cnt - 1) // 2) * (1 << bit)
        return total