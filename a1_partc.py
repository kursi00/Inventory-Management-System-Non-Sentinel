#    Main Author(s): Ahmed Kursi
#    Main Reviewer(s):



class Stack:
    def __init__(self, cap=10):
        self._data = [None] * cap  # Preallocate space with None
        self._size = 0             # Track the current number of elements
        self._capacity = cap       # Maximum capacity of the stack

    def capacity(self):
        return self._capacity

    def push(self, data):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)  # Double the capacity
        self._data[self._size] = data
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop() used on empty stack")
        self._size -= 1
        result = self._data[self._size]
        self._data[self._size] = None  # Clear the reference
        return result

    def get_top(self):
        if self.is_empty():
            return None
        return self._data[self._size - 1]

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def _resize(self, new_cap):
        new_data = [None] * new_cap
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_cap



class Queue:
    def __init__(self, cap=10):
        self._data = [None] * cap
        self._size = 0
        self._front = 0  # Points to the front of the queue
        self._capacity = cap

    def capacity(self):
        return self._capacity

    def enqueue(self, data):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        back = (self._front + self._size) % self._capacity  # Circular buffer
        self._data[back] = data
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue() used on empty queue")
        result = self._data[self._front]
        self._data[self._front] = None  # Clear the reference
        self._front = (self._front + 1) % self._capacity  # Circular buffer
        self._size -= 1
        return result

    def get_front(self):
        if self.is_empty():
            return None
        return self._data[self._front]

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def _resize(self, new_cap):
        new_data = [None] * new_cap
        for i in range(self._size):
            index = (self._front + i) % self._capacity
            new_data[i] = self._data[index]
        self._data = new_data
        self._front = 0
        self._capacity = new_cap


class Deque:
    def __init__(self, cap=10):
        self._data = [None] * cap
        self._front = 0
        self._size = 0
        self._capacity = cap

    def capacity(self):
        return self._capacity

    def push_front(self, data):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._front = (self._front - 1) % self._capacity  # Circular buffer
        self._data[self._front] = data
        self._size += 1

    def push_back(self, data):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        back = (self._front + self._size) % self._capacity
        self._data[back] = data
        self._size += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError('pop_front() used on empty deque')
        result = self._data[self._front]
        self._data[self._front] = None  # Clear the reference
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return result

    def pop_back(self):
        if self.is_empty():
            raise IndexError('pop_back() used on empty deque')
        back = (self._front + self._size - 1) % self._capacity
        result = self._data[back]
        self._data[back] = None  # Clear the reference
        self._size -= 1
        return result

    def get_front(self):
        if self.is_empty():
            return None
        return self._data[self._front]

    def get_back(self):
        if self.is_empty():
            return None
        back = (self._front + self._size - 1) % self._capacity
        return self._data[back]

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def _resize(self, new_cap):
        new_data = [None] * new_cap
        for i in range(self._size):
            index = (self._front + i) % self._capacity
            new_data[i] = self._data[index]
        self._data = new_data
        self._front = 0
        self._capacity = new_cap

    def __getitem__(self, k):
        if k < 0 or k >= self._size:
            raise IndexError('Index out of range')
        index = (self._front + k) % self._capacity
        return self._data[index]
