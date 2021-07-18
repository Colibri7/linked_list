class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        # head -> John -> None
        if self.head is None:
            self.head = newNode
        else:
            # head -> John -> Ben -> None || John -> Matthew

            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printlist(self):
        if self.head is None:
            print(f'List is empty')
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next


firstNode = Node('John')
linked_list = LinkedList()
linked_list.insert(firstNode)
secondNode = Node('Ben')
linked_list.insert(secondNode)
thirdNode = Node('Matthew')
linked_list.insert(thirdNode)
linked_list.printlist()
