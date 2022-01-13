class Node:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def list2link(list_):
    head = Node(list_[0])
    p = head
    for i in range(1, len(list_)):
        p.next = Node(list_[i])
        p = p.next
    return head

class Solution:
    # 206. Reverse Linked List
    # Given the head of a singly linked list, reverse the list,
    # and return the reversed list.
    # Input: head = [1,2,3,4,5]
    # Output: [5,4,3,2,1]
    # Input: head = [1,2]
    # Output: [2,1]
    # Input: head = []
    # Output: []

    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def reverseList2(self,head):
        def helper(head,node):
            if not head :
                return node
            tmp = head.next
            head.next = node
            return helper(tmp,head)
        return helper(head,None)



    # 141. Linked List Cycle
    # Given head, the head of a linked list, determine if the linked
    # list has a cycle in it.
    # Input: head = [3,2,0,-4], pos = 1
    # Output: true
    # Input: head = [1,2], pos = 0
    # Output: true
    # Input: head = [1], pos = -1
    # Output: false

    def hasCycle(self, head):
        seen = set()          #需要用node的地址来比较所以不用查看value
        while head:
            if head in seen:       #如果有一样的就返回
                return True
            seen.add(head)  #添加到set中
            head = head.next
        return False


    # 24. Swap Nodes in Pairs
    # Input: head = [1,2,3,4]
    # Output: [2,1,4,3]
    # Input: head = []
    # Output: []
    # Input: head = [1]
    # Output: [1]


    def swapPairs(self, head):
        dummy = Node(0,head)
        perv,curr = dummy,head
        while curr and curr.next:
            # save pointers
            nextpair = curr.next.next # 第二组node的开头
            secondnode = curr.next  #当前的第二个node
            # reverse this pair
            secondnode.next = curr #将第二个node指向第一个
            curr.next = nextpair    # curr成为这组的最后一个指向下一组的第一个
            perv.next = secondnode  # perv的next连接上现在的第一个secondnode

            # update pointer
            perv = curr     #perv 和 curr换位
            curr = nextpair  #
        return dummy.next

    # 328. Odd Even Linked List
    # Given the head of a singly linked list, group all the nodes with odd indices together
    # followed by the nodes with even indices, and return the reordered list.
    # Input: head = [1,2,3,4,5]
    # Output: [1,3,5,2,4]
    # Input: head = [2,1,3,5,6,4,7]
    # Output: [2,3,6,7,1,5,4]


    def oddEvenList(self, head):
        if not head or not head.next or head.next.next:
            return head
        oddptr = curr = head  #odd 的就是整个linked list的头
        evenptr = evenhead = head.next  # even 的头就是当前linked的第二个
        i=1
        while curr: #第一组不用算因为初始化所以从2开始
            if i>2 and i%2 !=0 :
                oddptr.next = curr
                oddptr = oddptr.next
            if i>2 and i%2 ==0:
                evenptr.next = curr
                evenptr = evenptr.next

            curr = curr.next #移动pointer
            i+=1
        evenptr.next = None #even的最后一个pointer指向None
        oddptr.next = evenhead  #odd pointer的最后一个指向even的头
        return head


    # 92. Reverse Linked List II
    # Input: head = [1,2,3,4,5], left = 2, right = 4
    # Output: [1,4,3,2,5]
    # Input: head = [5], left = 1, right = 1
    # Output: [5]

    def reverseBetween(self, head, left, right):
        dummy = Node(0,head)
        leftperv,cur = dummy ,head
        for i in range(left-1):         #找到最左边的前一个点
            leftperv,cur = cur,cur.next     #最左边的前一个点 cur是现在最左边需要换的点

        perv = None  #暂时设置前一个点为None
        for i in range(right-left+1):   # 总共要循环几次
            tmpnext = cur.next      # 将下一个指针保存好
            cur.next = perv         # 当前的next指向之前的node
            perv,cur = cur,tmpnext     #替换位置

        leftperv.next.next = cur        # 最右边 最左边的node与最后一个node连接
        leftperv.next = perv            # 最左边
        return dummy.next




object= Solution()
link206 = list2link([1,2,3,4,5])
link141 = list2link([3,2,0,-4])
print(object.reverseList(link206))
#print(object.hasCycle(link141))



