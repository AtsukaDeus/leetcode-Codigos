
class Node:
    
    def __init__(self, val):
        self.val = val
        self.ref = None 
        
        
        
class Solution:
    def isPalindrome(self, head):
        
        ListNode = []
        ListNodeCopy = []
        nextHead = head
        
        while nextHead!=None:
            ListNode.append(nextHead.val)
            nextHead = nextHead.ref
            
        for i in range(len(ListNode)-1, -1,-1):
            ListNodeCopy.append(ListNode[i])
        
        return ListNodeCopy == ListNode
            
    

if __name__ == "__main__":
    
    # Creando nodos
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(2)
    node4 = Node(1)

    # pasando las referencias para enlazar los nodos
    # a .ref le pasamos la direccion de memoria
    node1.ref = node2
    node2.ref = node3
    node3.ref = node4
    
    
    s = Solution()
    print(s.isPalindrome(node1))
    

        
        