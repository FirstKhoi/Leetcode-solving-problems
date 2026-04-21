class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def hashFunction(self, key):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hashFunction(key)
        node = self.table[index]

        if not node:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            prev = None
            curr = node
            while curr:
                if curr.key == key:
                    curr.value = value
                    return
                prev = curr
                curr = curr.next
            prev.next = Node(key, value)
            self.size += 1

        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hashFunction(key)
        node = self.table[index]

        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key: int) -> bool:
        index = self.hashFunction(key)
        node = self.table[index]
        prev = None

        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.table[index] = node.next
                self.size -= 1
                return True
            prev = node
            node = node.next
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        newCapacity = self.capacity * 2
        newTable = [None] * newCapacity

        for node in self.table:
            while node:
                index = node.key % newCapacity
                if not newTable[index]:
                    newTable[index] = Node(node.key, node.value)
                else:
                    newNode = newTable[index]
                    while newNode.next:
                        newNode = newNode.next
                    newNode.next = Node(node.key, node.value)
                node = node.next
        
        self.capacity = newCapacity
        self.table = newTable