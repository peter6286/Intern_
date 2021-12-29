# 节点类
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 树生成代码
def generate_tree(vals):
    if len(vals) == 0:
        return None
    que = [] # 定义队列
    fill_left = True # 由于无法通过是否为 None 来判断该节点的左儿子是否可以填充，用一个记号判断是否需要填充左节点
    for val in vals:
        node = Node(val) if val else None # 非空值返回节点类，否则返回 None
        if len(que)==0:
            root = node # 队列为空的话，用 root 记录根结点，用来返回
            que.append(node)
        elif fill_left:
            que[0].left = node
            fill_left = False # 填充过左儿子后，改变记号状态
            if node: # 非 None 值才进入队列
                que.append(node)
        else:
            que[0].right = node
            if node:
                que.append(node)
            que.pop(0) # 填充完右儿子，弹出节点
            fill_left = True #
    return root
# 定义一个dfs打印中序遍历
def dfs(node):
    if node is not None:
        dfs(node.left)
        print(node.val, end=' ')
        dfs(node.right)
# 定义一个bfs打印层序遍历
def bfs(node):
    que = []
    que.append(node)
    while que:
        l = len(que)
        for _ in range(l):
            tmp = que.pop(0)
            print(tmp.val, end=' ')
            if tmp.left:
                que.append(tmp.left)
            if tmp.right:
                que.append(tmp.right)
        print('|', end=' ')



class Solution:

    # 144. Binary Tree Preorder Traversal
    # Input: root = [1,null,2,3]
    # Output: [1,2,3]
    # Input: root = []
    # Output: []

    # 前序遍历：根结点、左子树、右子树

    def preorderTraversal( self,root):
        stack = [root]
        res = []
        while stack:
            temp = stack.pop()
            if temp:
                if isinstance(temp, Node):
                    stack.append(temp.right)
                    stack.append(temp.left)
                    stack.append(temp.val)
                else:
                    res.append(temp)
        return res


    # 94. Binary Tree Inorder Traversal
    # Input: root = [1,null,2,3]
    # Output: [1,3,2]
    # Input: root = []
    # Output: []
    # 中序遍历：左子树、根结点、右子树

    def inorderTraversal(self, root):
        stack = [root]
        res = []
        while stack:
            temp = stack.pop()
            if temp:
                if isinstance(temp, Node):
                    stack.append(temp.right)
                    stack.append(temp.val)
                    stack.append(temp.left)
                else:
                    res.append(temp)
        return res


    # 145. Binary Tree Postorder Traversal
    # Input: root = [1,null,2,3]
    # Output: [3,2,1]
    # Input: root = [1]
    # Output: [1]
    # 后序遍历：左子树、右子树、根结点
    def postorderTraversal(self, root):
        stack = [root]
        res = []
        while stack:
            temp = stack.pop()
            if temp:
                if isinstance(temp, Node):
                    stack.append(temp.val)
                    stack.append(temp.right)
                    stack.append(temp.left)
                else:
                    res.append(temp)
        return res


    # 102. Binary Tree Level Order Traversal
    # Input: root = [3,9,20,null,null,15,7]
    # Output: [[3],[9,20],[15,7]]
    # Input: root = [1]
    # Output: [[1]]

    def levelOrder(self, root):
        res = []  # Ans array
        if not root:
            return res
        q = []  # Queue for BFS
        q.append(root)
        while q:
            size = len(q)  # Get number of elements on level
            tmp = []  # Hold level temporarily
            for i in range(0, size):  # Empty entire level
                node = q.pop(0)
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(tmp)  # Dump level to res, we will now move onto the next level.
        return res



    # 100. Same Tree
    # Input: p = [1,2,3], q = [1,2,3]
    # Output: true
    # Input: p = [1,2], q = [1,null,2]
    # Output: false
    # Input: p = [1,2,1], q = [1,1,2]
    # Output: false

    def isSameTree(self, p, q):
        if q is None and p is None:
            return True
        elif q is None or p is None:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)







object=Solution()
null = None
vals = [3,9,20,null,null,15,7]
val2 = [1,2]
val3 = [1,null,2]
tree = generate_tree(vals)
tree2 = generate_tree(val2)
tree3 = generate_tree(val3)
print('中序遍历:')
dfs(tree) # 9 3 15 20 7
print('\n层序遍历:')
bfs(tree) # 3 | 9 20 | 15 7 |
print("\n")
print(object.preorderTraversal(tree))
print(object.inorderTraversal(tree))
print(object.postorderTraversal(tree))
print(object.levelOrder(tree))
print(object.isSameTree(tree2,tree3))
