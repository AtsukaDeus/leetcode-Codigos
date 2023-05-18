
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# recibe un nodo y retorna el nodo que esté en la mitad
# en caso de haber un numero par de nodos
# se retorna el de la derecha!
class Solution:
    def middleNode(self, head: Node) -> Node:
        node = head
        listNodes = []
        indexNode = 0
        while node != None:
            listNodes.append(node)
            node = node.next
        indexNode = int(len(listNodes)/2)
        node = listNodes[indexNode]
        return node
        


if __name__ == '__main__':
    
    # Creamos los nodos
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    
    # Pasamos las referencias
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    
    solution = Solution()
    print(solution.middleNode(node1))
    
