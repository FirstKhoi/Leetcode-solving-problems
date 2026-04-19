class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        if self.root == None:
            self.root = newNode
            return
        curr = self.root
        while True:
            if key < curr.key:
                if curr.left == None:
                    curr.left = newNode
                    return
                curr = curr.left
            elif key > curr.key:
                if curr.right == None:
                    curr.right = newNode
                    return
                curr = curr.right
            else:
                curr.val = val
                return


    def get(self, key: int) -> int:
        curr = self.root
        while curr != None:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        return -1

    def findingMin(self, node: TreeNode) -> TreeNode:
        while node and node.left:
            node = node.left
        return node

    def getMin(self) -> int:
        curr = self.findingMin(self.root)
        return curr.val if curr else -1

    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1

    def remove(self, key: int) -> None:
        self.root = self.removeFunc(self.root, key)
    
    def removeFunc(self, curr: TreeNode, key: int) -> TreeNode:
        if curr == None:
            return None
        
        if key > curr.key:
            curr.right = self.removeFunc(curr.right, key)
        
        elif key < curr.key:
            curr.left = self.removeFunc(curr.left, key)
        
        else: 
            if curr.left == None:
                return curr.right
            elif curr.right == None:
                return curr.left
            else:
                minNode = self.findingMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeFunc(curr.right, minNode.key)
        return curr
    def getInorderKeys(self) -> List[int]:
        res = []
        self.inorderTraversal(self.root, res)
        return res

    def inorderTraversal(self, root: TreeNode, res: List[int]) -> None:
        if root != None:
            self.inorderTraversal(root.left, res)
            res.append(root.key)
            self.inorderTraversal(root.right, res)