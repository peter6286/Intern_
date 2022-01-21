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


    # 237. Delete Node in a Linked List
    # Input: head = [4,5,1,9], node = 5
    # Output: [4,1,9]
    # Input: head = [4,5,1,9], node = 1
    # Output: [4,5,9]
    # https://leetcode.com/problems/delete-node-in-a-linked-list/
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


    # 19. Remove Nth Node From End of List
    # Input: head = [1,2,3,4,5], n = 2
    # Output: [1,2,3,5]
    # Input: head = [1], n = 1
    # Output: []
    # Input: head = [1,2], n = 1
    # Output: [1]
    # https://leetcode.com/problems/remove-nth-node-from-end-of-list/
    def removeNthFromEnd(self, head, n):
        slow,fast = head,head
        for i in range(n):
            fast = fast.next

        if not fast :
            return head.next

        while fast.next:
            slow =  slow.next
            fast = fast.next
        slow.next = slow.next.next

        return head


    # 83. Remove Duplicates from Sorted List
    # Given the head of a sorted linked list, delete all duplicates such that each
    # element appears only once. Return the linked list sorted as well.
    # Input: head = [1,1,2]
    # Output: [1,2]
    # Input: head = [1,1,2,3,3]
    # Output: [1,2,3]
    # https://leetcode.com/problems/remove-duplicates-from-sorted-list/

    def deleteDuplicates(self, head):
        curr = head
        while curr and curr.next :
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head



    # 203. Remove Linked List Elements
    # Input: head = [1,2,6,3,4,5,6], val = 6
    # Output: [1,2,3,4,5]
    # Input: head = [], val = 1
    # Output: []
    # Input: head = [7,7,7,7], val = 7
    # Output: []
    #  https://leetcode.com/problems/remove-linked-list-elements/

    def removeElements(self, head,val):
        dummy = Node(0,next = head)
        perv,curr = dummy ,head

        while curr:
            nxt = curr.next
            if curr.val == val:
                perv.next = nxt
            else:
                perv = curr
            curr = nxt
        return dummy.next


    # 82. Remove Duplicates from Sorted List II
    # Input: head = [1,2,3,3,4,4,5]
    # Output: [1,2,5]
    # Input: head = [1,1,1,2,3]
    # Output: [2,3]
    # https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

    def deleteDuplicates(self, head):
        dummy = Node(0,next=head)
        perv ,curr = dummy ,head
        while curr:
            if curr.next and curr.val == curr.next.val: #检查有没有重复的
                while curr.next and curr.val == curr.next.val:  #跳到没有重复的点上
                    curr = curr.next
                perv.next = curr.next       #将前面的点和没重复的连上
            else:
                perv = perv.next        #如果没有重复的时候perv就是下一个点
            curr = curr.next
        return dummy.next


    # 2. Add Two Numbers
    # Input: l1 = [2,4,3], l2 = [5,6,4]
    # Output: [7,0,8]
    # Explanation: 342 + 465 = 807.
    # Input: l1 = [0], l2 = [0]
    # Output: [0]
    # Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    # Output: [8,9,9,9,0,0,0,1]
    # https://leetcode.com/problems/add-two-numbers/


    def addTwoNumbers(self, l1, l2):
        dummy = Node()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry   #将值加起来
            carry = val // 10       # carry 是数值除后
            val = val % 10          # node里面的val用%
            curr.next = Node(val)

            # updates pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next



    # 160. Intersection of Two Linked Lists
    # Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
    # Output: Intersected at '8'
    # https://leetcode.com/problems/intersection-of-two-linked-lists/


    def getIntersectionNode(self,headA,headB):
        # L1 = 1,2,3
        # L2 = 6,5,2,3
        #
        # L1+L2 = 1,2,3,6,5,2,3
        # L2+L1 = 6,5,2,3,1,2,3


        l1,l2 = headA,headB
        while l1 != l2 :  #l1 和 l2 互相不等的时候继续循环到下一个点 equal的情况是找到点上了  一直找到最后一个点也是Null
            l1=l1.next if l1 else headB #加起来会让有相同的点连接起来
            l2=l2.next if l2 else headA
        return l1




    # 21. Merge Two Sorted Lists
    # Input: list1 = [1,2,4], list2 = [1,3,4]
    # Output: [1,1,2,3,4,4]
    # Input: list1 = [], list2 = []
    # Output: []
    # Input: list1 = [], list2 = [0]
    # Output: [0]
    # https://leetcode.com/problems/merge-two-sorted-lists/

    def mergeTwoLists(self, list1, list2):
        dummy = Node()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1   #下一个连接上的是较小的node
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next    #tail也要随之移动

        if list1:           #如果其中一个是空的让tail将剩下的连接上
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

    # 234. Palindrome Linked List
    # Given the head of a singly linked list, return true if it is a palindrome.
    # Input: head = [1,2,2,1]
    # Output: true
    # Input: head = [1,2]
    # Output: false

    def isPalindrome(self, head):
        fast,slow = head,head
        # find middle pointer (slow)  fast是slow的两倍所以slow刚好会在listnode的中间
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse the second half of the node 利用刚刚设定好的slow pointer
        perv = None
        while slow:
            temp = slow.next
            slow.next = perv
            perv = slow
            slow = temp

        # check palindrome
        left,right = head,perv
        while right:        # right 的最后是个None
            if right.val != left.val:
                return False
            left = left.next
            right = right.next
        return True



    # 143. Reorder List
    # Input: head = [1,2,3,4]
    # Output: [1,4,2,3]
    # Input: head = [1,2,3,4,5]
    # Output: [1,5,2,4,3]
    # https://leetcode.com/problems/reorder-list/
    def reorderList(self, head):

        # find middle
        slow ,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        perv = slow.next = None
        while second:
            temp = second.next
            second.next = perv
            perv = second
            second = temp

        # merge two halfs
        left,right = head,perv
        while right:
            temp1,temp2=left.next,right.next
            left.next = right
            right.next = temp1
            left,right = temp1,temp2


    # 142. Linked List Cycle II
    # Input: head = [3,2,0,-4], pos = 1
    # Output: tail connects to node index 1
    # Input: head = [1,2], pos = 0
    # Output: tail connects to node index 0
    # Input: head = [1], pos = -1
    # Output: no cycle
    # https://leetcode.com/problems/linked-list-cycle-ii/
    def detectCycle(self,head):

        # Two points both start off at the head node, one pointer moves one step at a time, while
        # the other pointer moves two steps at a time. If there is a cycle the two pointers will meet
        # at some point.
        slow,fast = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        else:
            return None
        # Use the previous fast pointer and a new pointer which starts at head. Move each of the pointers
        # by one step, the point where the two pointers meets will be the start of the cycle.
        pointer = head
        while pointer != fast :
            pointer = pointer.next
            fast = fast.next

        return pointer


    # 148. Sort List
    def sortList(self, head):
        # 找中间的点
        def findmid(head):
            slow,fast = head,head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        # merge
        def merge(list1,list2):
            tail = dummy = Node()
            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail=tail.next
            if list1:
                tail.next = list1
            if list2:
                tail.next = list2

            return dummy.next

        if not head or not head.next:
            return head
        left = head
        right = findmid(head)     # mid 是中间的下一个点所以得移动
        tmp = right.next
        right.next = None       #先将目前的点的next 切断
        right = tmp             #再将right移动到下一个点
        left = self.sortList(left)
        right = self.sortList(right)
        return merge(left,right)



    def rotateRight(self, head, k):
        if not head:
            return head

        # 找到长度和最后的那个node
        length,tail = 1,head
        while tail.next:
            tail = tail.next
            length += 1

        # 看是否需要rotate
        k = k % length
        if k==0:
            return head

        # move to the pivot and rotate
        cur = head
        for i in ragne (length-k-1):
            cur = cur.next
        newhead = cur.next
        cur.next = None
        tail.next = head
        return newhead





















object= Solution()
link206 = list2link([1,2,3,4,5])
link141 = list2link([3,2,0,-4])
link1 = list2link([1,9,1,2,4])
link2 = list2link([3,2,4])
print(object.reverseList(link206))
#print(object.hasCycle(link141))
print(object.getIntersectionNode(link1,link2))



