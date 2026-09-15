class Solution:
    def getCount(self, root, k):
        costs = []
        q = [(root, 1)]

        while q:
            node, level = q.pop(0)

            if node.left is None and node.right is None:
                costs.append(level)

            if node.left:
                q.append((node.left, level + 1))

            if node.right:
                q.append((node.right, level + 1))

        costs.sort()

        ans = 0

        for cost in costs:
            if cost <= k:
                k -= cost
                ans += 1
            else:
                break

        return ans