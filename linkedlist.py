class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addHead(self, n):
        new_node = Node(n)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def printNode(self):
        temp=self.head
        while temp is not None:
            print(temp.value,end="->")
            temp = temp.next
        print(None)
    def printMiddle(self):
        n1=self.head
        n2=self.head
        while n2 is not None and n2.next is not None:
            n1= n1.next
            n2=n2.next.next
        print(n1.value)
    def countNodes(self):
        count=0
        t=self.head
        while t is not None:
            count+=1
            t=t.next
        return count
#code for transforming linked list to BST
def sortedBst(head):
    n=head.countNodes()
    return  sortedBstRecur(head,n)
def sortedBstRecur(head,n):
    if n<=0:
        return None
    left=sortedBstRecur(head,n//2)

    root=Node(head.value)
    root.left=left
    head=head.next
    root.right=sortedBstRecur(head,n-n//2-1)
    return root
#code ends here

if __name__ == "__main__":
    l = LinkedList()
    l.addHead(4)
    l.addHead(5)
    l.addHead(6)
    l.addHead(3)
    l.printNode()
    l.printMiddle()
    print(l.countNodes())
