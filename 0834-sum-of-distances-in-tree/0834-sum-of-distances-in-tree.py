class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        result = [0] * n
        count = [1] * n
        tree = collections.defaultdict(set)

        for u, v in edges:
            tree[u].add(v)
            tree[v].add(u)

        def postorder(node, parent=None):
            for child in tree[node]:
                if child == parent:
                    continue
                postorder(child, node)
                count[node] += count[child]
                result[node] += result[child] + count[child]

        def preorder(node, parent=None):
            for child in tree[node]:
                if child == parent:
                    continue
                result[child] = result[node] - count[child] + (n - count[child])
                preorder(child, node)

        postorder(0)
        preorder(0)
        return result