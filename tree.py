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
        if not root.left and not root.right: # base case leaf node 也是1
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
            balance = (left[0] and right[0] and abs(left[1]-right[1])<=1)  # 判断是不是balance
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
        res = res[::-1]  #把结果反过来即可
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
                node = q.pop(0)         # node一直会到这一层的最右边所以val一直会变
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
            left = dfs(node.left)           # 先用dfs找到他们的位置
            right = dfs(node.right)
            cur = node == p or node == q  #当其中有一个点等于p 或 q 时
            if (left and right) or (cur and left) or (cur and right): # this node is the ancestor
                self.ans = node
                return                  #dfs中点会回跳所以curr会回到ancestor上
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


    # 99. Recover Binary Search Tree
    # Input: root = [1,3,null,null,2]
    # Output: [3,1,null,null,2]
    # Explanation: 3 cannot be a left child of 1 because 3 > 1.
    # Swapping 1 and 3 makes the BST valid.
    # Input: root = [3,1,4,null,null,2]
    # Output: [2,1,4,null,null,3]
    # Explanation: 2 cannot be in the right subtree of 3 because 2 < 3.
    # Swapping 2 and 3 makes the BST valid.

    def recoverTree(self, root):
        stack = []
        replace = []
        perv = Node(float("-inf"))
        curr = root
        while curr or stack:
            while curr:             # inorder traversal
                stack.append(curr)
                curr = curr.left
            temp = stack.pop()
            if temp.val < perv.val:     # 在inorder 里当前的value一定是要比perv的大所以进入replace
                replace.append((perv,temp)) # 【(3,2),(2,1)] 所以第一个要和最后一个node换

            perv = temp
            curr = temp.right
            # 在replace的list中替换这两个点
            replace[0][0].val, replace[-1][1].val = replace[-1][1].val, replace[0][0].val

    # 114. Flatten Binary Tree to Linked List
    # Input: root = [1,2,5,3,4,null,6]
    # Output: [1,null,2,null,3,null,4,null,5,null,6]
    # Input: root = []
    # Output: []
    # Input: root = [0]
    # Output: [0]


    def flatten(self, root):
        def dfs(root):
            if not root:
                return None

            Lefttail = dfs(root.left)
            Righttail = dfs(root.right)

            if root.left: #如果有左树的时候
                Lefttail.right = root.right     #将左树的尾巴和右树的头给连上
                root.right = root.left          # 右树的头和左树连接上
                root.left = None
            last = Righttail or Lefttail or root #因为所有都在右树上先返回右树再or其他的点
            return last
        dfs(root)


    # 222. Count Complete Tree Nodes
    # Input: root = [1,2,3,4,5,6]
    # Output: 6
    # Input: root = []
    # Output: 0
    # Input: root = [1]
    # Output: 1
    def countNodes(self, root):
        def getdepth(root):
           if not root:
               return 0
           return 1+getdepth(root.left)   #因为是从左到右的顺序所以getdepth也是找最后一个左树
        if not root:
            return 0
        leftdepth = getdepth(root.left)     #找深度
        rightdepth = getdepth(root.right)
        if leftdepth == rightdepth:
            return pow(2,leftdepth)+self.countNodes(root.right)  # the left sub tree is a full binary tree
        else:
            return pow(2,rightdepth)+self.countNodes(root.left) # the right sub tree is a full binary tree


    # 105. Construct Binary Tree from Preorder and Inorder Traversal
    # Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    # Output: [3,9,20,null,null,15,7]
    # Input: preorder = [-1], inorder = [-1]
    # Output: [-1]


    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root = Node(preorder[0])
        mid = inorder.index([preorder[0]]) #用mid把左树右树分开
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root


    # 116. Populating Next Right Pointers in Each Node
    # Populate each next pointer to point to its next right node.
    # If there is no next right node,the next pointer should be set to NULL.
    # Input: root = [1,2,3,4,5,6,7]
    # Output: [1,#,2,3,#,4,5,6,7,#]

    def connect(self, root):                  # bfs queue
        if not root:
            return root
        q = []
        q.append(root)
        while q :
            curr = q.pop(0)
            if curr.left and curr.right:  #将current的左右子树连接上
                curr.left.next = curr.right
                if curr.next:       #如果current有next代表同一层有边还有一个node将他们连接上
                    curr.right.next = curr.next.left    #curr的右子树连接上curr同一层右边的node的左子树
                q.append(curr.left)
                q.append(curr.right)

        return root


    # 117. Populating Next Right Pointers in Each Node II
    # Input: root = [1,2,3,4,5,null,7]
    # Output: [1,#,2,3,#,4,5,7,#]
    #  https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

    def connect2(self, root):
        if not root:
            return root
        q = []
        q.append(root)
        tail = root
        while q:
            curr = q.pop()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            if curr == tail:            #检查是不是在这一层的最后一个元素
                curr.next =None         #将最后一个指向None
                tail = q[-1] if len(q) > 0 else None    #更新新的tail为queue中的最后一个元素下一层的最后一个
            else:
                curr.next = q[0]
        return root


    # 96. Unique Binary Search Trees
    # Input: n = 3
    # Output: 5
    #  Input: n = 1
    # Output: 1
    # https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

    # numTree[4] = numTree[0] * numTree[3]
    #            = numTree[1] * numTree[2]
    #            = numTree[2] * numTree[1]
    #            = numTree[3] * numTree[0]

    def numTrees(self, n):
        numtree = [1] *(n+1)        #dynamic programming 把到n为止的解算出

        # base case
        # 0 nodes = 1 tree
        # 1 nodes = 1 tree
        # 所以找解的dynamic programming 从2开始（0，1都不算）
        for nodes in range(2,n+1):
            total = 0       #临时存0
            for root in range(1,nodes+1):       #每个node作为root
                left = root - 1
                right = nodes - root
                total += numtree[left] * numtree[right] #在里面找对应的后乘起来因为是combination
            numtree[nodes] = total
        return numtree[n]


    # 95. Unique Binary Search Trees II
    # Input: n = 3
    # Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
    # https://leetcode.com/problems/unique-binary-search-trees-ii/

    # backtracking
    def numgenerateTrees(self, n):
        def dfs(st,end):        #edge case 如果start 大于 end
            if st > end :
                return [None]
            ans = []
            for i in range(st,end+1):   # i 现在遍历的node value
                left = dfs(st,i-1)      # 当前点的左边去左树
                right = dfs (i+1,end)   # 当前点的右边去右树
                for l in left :         # 先左树再右树
                    for r in right:
                        root = Node(i)
                        root.left = l
                        root.right = r
                        ans.append(root)
            return ans
        return (1,n)




    # 331. Verify Preorder Serialization of a Binary Tree
    # Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    # Output: true
    # Input: preorder = "1,#"
    # Output: false
    # Input: preorder = "9,#,#,1"
    # Output: false
    # https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/


    def isValidSerialization(self, preorder):
        stack = []
        for n in preorder.split(","):       #用split隔开循环
            stack.append(n)
            # 连续出现三个#是肯定不对的
            # stack最后两个item出现是#的时候说明是leaf node
            # 将item pop出node用#代表进行下一层的检查
            while len(stack)> 2 and stack[-2::]==["#"]*2 and stack[-3]!="#":
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append("#")
        return stack == ["#"]


































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
# tree99 = generate_tree([1,3,null,null,2])
tree114 = generate_tree([1,2,5,3,4,null,6])
tree222 = generate_tree([[1,2,3,4,5,6]])

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
print(object.flatten(tree114))
print(object.countNodes(tree222))



