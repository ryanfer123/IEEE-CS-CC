class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def insert_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
    
    def traverse_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=' <-> ')
            temp = temp.next
        print('None')
    
    def traverse_backward(self):
        temp = self.head
        if temp is None:
            return
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=' <-> ')
            temp = temp.prev
        print('None')

# User Input
dll = DoublyLinkedList()
while True:
    print("\nOptions: 1. Insert Head  2. Insert Tail  3. Traverse Forward  4. Traverse Backward  5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter value to insert at head: "))
        dll.insert_head(data)
    elif choice == 2:
        data = int(input("Enter value to insert at tail: "))
        dll.insert_tail(data)
    elif choice == 3:
        dll.traverse_forward()
    elif choice == 4:
        dll.traverse_backward()
    elif choice == 5:
        break
    else:
        print("Invalid choice, please try again.")
