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
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

    def reverseList2(self,head):
        def helper(head,node):
            if not head :
                return node
            tmp = head.next
            head.next = node
            return helper(tmp,head)
        return helper(head,None)


object= Solution()
link206 = list2link([1,2,3,4,5])
print(object.reverseList(link206))



