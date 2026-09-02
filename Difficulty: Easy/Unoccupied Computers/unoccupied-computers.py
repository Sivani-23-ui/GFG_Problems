class Solution:
    def solve(self, n, s):
        # code here
        occ = 0
        inside = set()
        rej = set()

        for ch in s:
            if ch not in inside:   # arrival
                if occ < n:
                    occ += 1
                    inside.add(ch)
                else:
                    rej.add(ch)
                    inside.add(ch)  # still mark them inside so we know when they leave
            else:                  # departure
                if ch not in rej:
                    occ -= 1
                inside.remove(ch)

        return len(rej)