class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.base = 769
        self.data = [[] for _ in range(self.base)]

    def add(self, key: int) -> None:
        hashkey = self.hash(key)
        if key in self.data[hashkey]:
            return
        self.data[hashkey].append(key)

    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        if key not in self.data[hashkey]:
            return
        self.data[hashkey].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashkey = self.hash(key)
        return key in self.data[hashkey]

    def hash(self,key):
        return key % self.base
