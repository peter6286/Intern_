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

    # 101. Symmetric Tree
    # Input: root = [1,2,2,3,4,4,3]
    # Output: true
    # Input: root = [1,2,2,null,3,null,3]
    # Output: false

    def isSymmetric(self, root):
        if not root:
            return False
        def helper(l, r):
            if not l and not r:
                return True
            if l and r and l.val == r.val:
                return helper(l.left, r.right) and helper(l.right, r.left)

        return helper(root, root)

    def isSymmetric2(self, root):
        queue = [(root, root)]
        while queue:
            l, r = queue.pop(0)
            if l is None and r is None:
                continue
            if l is None or r is None:
                return False
            if l.val == r.val:
                queue.append((l.left, r.right))
                queue.append((l.right, r.left))
            else:
                return False
        return True

    # 226. Invert Binary Tree
    # Input: root = [4,2,7,1,3,6,9]
    # Output: [4,7,2,9,6,3,1]
    # Input: root = [2,1,3]
    # Output: [2,3,1]
    # Input: root = []
    # Output: []

    def invertTree(self, root):
        if not root :
            return None
        temp = root.left        #左右互换
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)      #在node上的每个节点上互换
        self.invertTree(root.right)
        return root

    # 257. Binary Tree Paths
    # Input: root = [1,2,3,null,5]
    # Output: ["1->2->5","1->3"]
    # Input: root = [1]
    # Output: ["1"]

    def binaryTreePaths(self, root):
        res = []
        stack = [(root,str(root.val))]

        while stack:
            curr,path = stack.pop()
            if curr:
                if curr != root : #如果不是root的话进入输出加上符号
                    path += '->' + str(curr.val)
                if curr.right:
                    stack.append((curr.right,path))
                if curr.left :
                    stack.append((curr.left,path))
                if not curr.right and not curr.left :
                    res.append(path)     #左右两边tree都结束了的时候将path压入res
        return res



    # 112. Path Sum
    # Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    # Output: true
    # Input: root = [1,2,3], targetSum = 5
    # Output: false
    # Input: root = [], targetSum = 0
    # Output: false

    # Iteratively:
    def hasPathSum(self, root, targetSum):
        stack = [(root, targetSum - root.val)]
        while stack:
            curr,curr_sum = stack.pop()
            if not curr.left and not curr.right and curr_sum == 0 : #如果等于0的时候输出
                return True
            if curr.right :             # 往两边的sub leaf减直到等于0
                stack.append((curr.right,curr_sum-curr.right.val))
            if curr.left:
                stack.append((curr.left,curr_sum-curr.left.val))
        return False


    # recursively:
    def hasPathSum1(self, root, targetSum):
        if not root:
            return False
        targetSum -= root.val
        if not root.left and root.right :       #base case
            return targetSum== 0
        return self.hasPathSum1(root.left,targetSum) or self.hasPathSum1(root.right,targetSum)


    # 113. Path Sum II
    # Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    # Output: [[5,4,11,2],[5,8,4,5]]
    # Input: root = [1,2,3], targetSum = 5
    # Output: []
    # Input: root = [1,2], targetSum = 0
    # Output: []

    def pathSum(self, root, targetSum):
        ans = []
        def dfs(node,curr_path,target):
            # base case to stop condition
            if not node:
                return
            target -= node.val      #更新现在target的值
            if not node.left and not node.right and target == 0:
                # 检查leaf node 如果到达最底层等于0进入输出
                curr_path.append(node.val)
                ans.append(curr_path)
                return
            # dfs
            dfs(node.left,curr_path+[node.val],target)
            dfs(node.right,curr_path+[node.val],target)
            return
        dfs(root,[],targetSum)
        return ans

    # 129. Sum Root to Leaf Numbers
    # Input: root = [1,2,3]
    # Output: 25
    # Input: root = [4,9,0,5,1]
    # Output: 1026

    def sumNumbers(self, root):
        def dfs(curr,num):
            if not curr :
                return 0

            num = num *10 + curr.val   #乘10后加刚好进位到下一位然后加上数
            if not curr.left and not curr.right :
                return num
            return dfs(curr.left,num)+dfs(curr.right,num)   #把值加起来
        return dfs(root,0)


    # 111. Minimum Depth of Binary Tree
    # Input: root = [3,9,20,null,null,15,7]
    # Output: 2
    # Input: root = [2,null,3,null,4,null,5,null,6]
    # Output: 5

    def minDepth(self, root):   #用level来分开做sub-tree 用dfs循环从下往上算出来
        if not root :
            return 0
        if not root.left and not root.right:
            return 1

        if not root.left and root.right:    #只有右边有
            return 1+ self.minDepth(root.right)

        if not root.right and root.left:    #只有左边有
            return 1+self.minDepth(root.left)

        return min(1+self.minDepth(root.left),1+self.minDepth(root.right))



    # 104. Maximum Depth of Binary Tree
    # Input: root = [3,9,20,null,null,15,7]
    # Output: 3
    # Input: root = [1,null,2]
    # Output: 2

    def maxDepth(self, root):
        if not root :
            return 0
        if not root.left and not root.right:
            return 1

        if not root.left and root.right:    #只有右边有
            return 1+ self.minDepth(root.right)

        if not root.right and root.left:    #只有左边有
            return 1+self.minDepth(root.left)

        return max(1+self.minDepth(root.left),1+self.minDepth(root.right))



    # 110. Balanced Binary Tree
    # Input: root = [3,9,20,null,null,15,7]
    # Output: true
    # Input: root = [1,2,2,3,3,null,null,4,4]
    # Output: false
    # Input: root = []
    # Output: true

    def isBalanced(self, root):
        def dfs(root):          #从下往上的结构
            if not root :
                return [True,0]
            left,right = dfs(root.left),dfs(root.right)  #往两边search
            balance = (left[0] and right[0] and abs(left[0]-left[1])<=1)  # 判断是不是balance
            return [balance,1+max(left[1],right[1])]  #把深度继续加上去
        return dfs(root)[0]


    # 337. House Robber III
    # Input: root = [3,2,3,null,3,null,1]
    # Output: 7
    # Input: root = [3,4,5,1,3,null,1]
    # Output: 9
    def rob(self, root):        #从下往上的结构
        # return pair: [withroot,withoutroot]
        def dfs(root):
            if not root :
                return [0,0]
            leftpair = dfs(root.left)
            rightpair = dfs (root.right)
            withnode = root.val + leftpair[1] + rightpair[1] # [1]代表withoutnode的pair
            withoutnode = max(leftpair) + max (rightpair)   # 选最大的点
            return [withnode,withoutnode]
        return max(dfs(root))


    # 107. Binary Tree Level Order Traversal II
    # Input: root = [3,9,20,null,null,15,7]
    # Output: [[15,7],[9,20],[3]]
    # Input: root = [1]
    # Output: [[1]]
    # Input: root = []
    # Output: []

    def levelOrderBottom(self, root):
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
        res = res[::-1]
        return res


    # 103. Binary Tree Zigzag Level Order Traversal
    # Input: root = [3,9,20,null,null,15,7]
    # Output: [[3],[20,9],[15,7]]
    # Input: root = [1]
    # Output: [[1]]
    # Input: root = []
    # Output: []
    def zigzagLevelOrder(self, root):
        res = []  # Ans array
        if not root:
            return res
        q = []  # Queue for BFS
        q.append(root)
        level = 1
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

            if level % 2 == 0 :
                res.append(tmp[::-1])
            else :
                res.append(tmp)
            level+=1
        return res

    # 199. Binary Tree Right Side View
    # Input: root = [1,2,3,null,5,null,4]
    # Output: [1,3,4]
    # Input: root = [1,null,3]
    # Output: [1,3]
    # Input: root = []
    # Output: []

    def rightSideView(self, root):
        res = []  # Ans array
        if not root:
            return res
        q = []  # Queue for BFS
        q.append(root)
        while q:
            size = len(q)  # Get number of elements on level
            val = 0
            for i in range(0, size):  # Empty entire level
                node = q.pop(0)
                val = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(val)
        return res


    # 98. Validate Binary Search Tree
    # Input: root = [2,1,3]
    # Output: true
    # Input: root = [5,1,4,null,null,3,6]
    # Output: false

    def isValidBST(self, root):
        def valid(node,left,right):  # 从下往上的结构
            if not node:
                return True
            if not (node.val < right and node.val > left ): #如果中间的node小于右边 当前的node大于左边的
                return False
            return (valid(node.left,left,node.val) and valid(node.right,node.val,right))
        # 当是左树的时候，右边的上限更新为现在的点。当时右树的时候，左边的下限更新为现在大的点
        return valid(root,float("-inf"),float("inf"))





    # 235. Lowest Common Ancestor of a Binary Search Tree
    # Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    # Output: 6
    # Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    # Output: 2

    def lowestCommonAncestor(self, root, p, q):
        cur = root
        while cur :
            if p.val > cur.val and q.val > cur.val:     #node 都比现在的大往右树找lowest common ancestor
                cur=cur.right
            elif p.val < cur.val and p.val < cur.val:   #node 都比现在的小往左树找lowest common ancestor
                cur = cur.left
            else:           #其他的情况都可以确定为当前的node是lowest common ancestor
                return cur


    # 236. Lowest Common Ancestor of a Binary Tree
    # Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    # Output: 3
    # Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    # Output: 5

    def lowestCommonAncestor2(self, root, p, q):
        self.ans = None
        def dfs(node):
            if not node :
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            cur = node == p or node == q  #当其中有一个点等于p 或 q 时
            if (left and right) or (cur and left) or (cur and right):
                self.ans = node
                return
            return left or right or cur
        dfs(root)
        return self.ans


    # 108. Convert Sorted Array to Binary Search Tree
    # Input: nums = [-10,-3,0,5,9]
    # Output: [0,-3,9,-10,null,5]
    # Input: nums = [1,3]
    # Output: [3,1]
    def sortedArrayToBST(self, nums):
        def helper (left,right):
            if left > right: #当左边的比右边大的时候是edge case
                return None
            mid = (left+right)//2       #往中间切割
            root = Node(nums[mid])  #设置当前的这个点
            root.left = helper(left,mid-1)      #left比现在的这个点小所以都是mid的左边
            root.right = helper(mid+1,right)    #right比现在的这个点大所以都是mid的右边
            return root
        return helper(0,len(nums)-1)



    # 109. Convert Sorted List to Binary Search Tree
    # Input: head = [-10,-3,0,5,9]
    # Output: [0,-3,9,-10,null,5]
    # Input: head = []
    # Output: []

    def sortedListToBST(self, head):
        if not head:
            return
        if not head.next:
            return Node(head.val)
        slow,fast = head,head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        temp = slow.next
        slow.next = None
        root = Node(temp.val)
        root.left=self.sortedListToBST(head)
        root.right=self.sortedListToBST(temp)
        return root

    # 173. Binary Search Tree Iterator
    # Implement the BSTIterator class that represents an
    # iterator over the in-order traversal of a binary search tree (BST):
    # Input
    # ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
    # [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
    # Output
    # [null, 3, 7, true, 9, true, 15, true, 20, false]


    # Explanation
    # BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
    # bSTIterator.next();    // return 3
    # bSTIterator.next();    // return 7
    # bSTIterator.hasNext(); // return True
    # bSTIterator.next();    // return 9
    # bSTIterator.hasNext(); // return True
    # bSTIterator.next();    // return 15
    # bSTIterator.hasNext(); // return True
    # bSTIterator.next();    // return 20
    # bSTIterator.hasNext(); // return False

    class BSTIterator(object):
        def __init__(self, root):  #先将左边的leaf node全部加进去
            self.stack=[]
            while root:
                self.stack.append(root)
                root=root.left


        def next(self):
            node =self.stack.pop()  #用pop()回到上一个点再往右边循环一样先把左边的leaf node全部加进去
            x = node.right
            while x :
                self.stack.append(x)
                x=x.left
            return node.val

        def hasnext(self):      #当stack没有元素时是空的
            return len(self.stack)>0


    # 230. Kth Smallest Element in a BST
    # Input: root = [3,1,4,null,2], k = 1
    # Output: 1
    # Input: root = [5,3,6,2,4,null,null,1], k = 3
    # Output: 3

    def kthSmallest(self, root, k):
        stack = []
        while root or stack:
            while root:         #因为是要找最小的所以一直在left subtree上找直到找到null的左树
                stack.append(root)
                root = root.left
            root = stack.pop()  # 返回最后一个node
            k -= 1
            if k == 0:
                return root.val
            root = root.right       #如果不成立再往右树上找然后循环


























object=Solution()
null = None
vals = [3,9,20,null,null,15,7]
val2 = [1,2]
val3 = [1,null,2]
tree = generate_tree(vals)
tree2 = generate_tree(val2)
tree3 = generate_tree(val3)
tree101 = generate_tree([1,2,2,3,4,4,3])
tree226 = generate_tree([4,2,7,1,3,6,9])
tree257 = generate_tree([1,2,3,null,5])
tree112 = generate_tree([5,4,8,11,null,13,4,7,2,null,null,null,1])
tree113 = generate_tree([5,4,8,11,null,13,4,7,2,null,null,5,1])
tree129 = generate_tree([1,2,3])
tree111 = generate_tree([3,9,20,null,null,15,7])
tree104 = generate_tree([3,9,20,null,null,15,7])
tree110 = generate_tree([3,9,20,null,null,15,7])
tree337 = generate_tree([3,2,3,null,3,null,1])
tree107 = generate_tree([3,9,20,null,null,15,7])
tree103 = generate_tree([3,9,20,null,null,15,7])
tree199 = generate_tree([1,3])
tree98 = generate_tree([5])
tree235 = generate_tree([6,2,8,0,4,7,9,null,null,3,5])

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
print(object.isSymmetric(tree101))
print(object.invertTree(tree226))
print(object.binaryTreePaths(tree257))
print(object.hasPathSum(tree112,22))
print(object.pathSum(tree113,22))
print(object.sumNumbers(tree129))
print(object.minDepth(tree111))
print(object.maxDepth(tree104))
print(object.isBalanced(tree110))
print(object.rob(tree337))
print(object.levelOrderBottom(tree107))
print(object.zigzagLevelOrder(tree107))
print(object.rightSideView(tree199))
print(object.isValidBST(tree98))
# print(object.lowestCommonAncestor(tree235,2,8))


