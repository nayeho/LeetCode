class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.word: Optional[str] = None

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = []
        root = TrieNode()

        def insert(word: str) -> None:
            node = root
            for c in word:
                node = node.children.setdefault(c, TrieNode())
            node.word = word

        def search(node: Optional[TrieNode]) -> List[str]:
            res: List[str] = []
            dfs(node, res)
            return res

        def dfs(node: Optional[TrieNode], res: List[str]) -> None:
            if len(res) == 3:
                return
            if not node:
                return
            if node.word:
                res.append(node.word)
            for c in string.ascii_lowercase:
                if c in node.children:
                    dfs(node.children[c], res)

        for product in products:
            insert(product)

        node = root

        for c in searchWord:
            if not node or c not in node.children:
                node = None
                result.append([])
                continue
            node = node.children[c]
            result.append(search(node))

        return result