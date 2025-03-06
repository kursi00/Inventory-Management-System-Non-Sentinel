#    Main Author(s): Ahmed Kursi
#    Main Reviewer(s): Ahmed Kursi




class SortedList:
    class Node:
        def __init__(self, data, next=None, prev=None):
            # Initialize node with data and pointers to next and previous nodes
            self.data = data
            self.next = next
            self.prev = prev

        def get_data(self):
            # Return the data stored in the node
            return self.data

        def get_next(self):
            # Return the next node
            return self.next

        def get_previous(self):
            # Return the previous node
            return self.prev

    def __init__(self):
        # Initialize an empty sorted list
        self.head = None  # Reference to the first node
        self.tail = None  # Reference to the last node
        self.size = 0     # Number of elements in the list

    def get_front(self):
        # Return the head node (front of the list)
        return self.head

    def get_back(self):
        # Return the tail node (end of the list)
        return self.tail

    def is_empty(self):
        # Check if the list is empty
        return self.size == 0

    def __len__(self):
        # Return the number of elements in the list
        return self.size

    def insert(self, data):
        # Insert a new node with the given data in sorted order
        new_node = self.Node(data)
        # If the list is empty
        if self.head is None:
            self.head = self.tail = new_node  # New node becomes both head and tail
        else:
            current = self.head
            # Traverse to find the correct insertion point
            while current and current.data < data:
                current = current.get_next()

            if current is None:  # Insert at the end
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            elif current == self.head:  # Insert at the front
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            else:  # Insert in the middle
                prev_node = current.get_previous()
                prev_node.next = new_node
                new_node.prev = prev_node
                new_node.next = current
                current.prev = new_node

        self.size += 1  # Increment the size of the list
        return new_node

    def erase(self, node):
        # Remove a node from the list
        if node is None:
            raise ValueError('Cannot erase node referred to by None')

        # If the node is the only element in the list
        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            # If the node is at the front, update head
            self.head = node.get_next()
            if self.head:
                self.head.prev = None
        elif node == self.tail:
            # If the node is at the end, update tail
            self.tail = node.get_previous()
            if self.tail:
                self.tail.next = None
        else:
            # If the node is in the middle, adjust pointers of adjacent nodes
            prev_node = node.get_previous()
            next_node = node.get_next()
            prev_node.next = next_node
            next_node.prev = prev_node

        self.size -= 1  # Decrement the size of the list

    def search(self, data):
        # Find the first node containing the given data
        current = self.head
        while current:
            if current.get_data() == data:
                return current  # Return the found node
            current = current.get_next()
        return None  # Return None if the data is not found
