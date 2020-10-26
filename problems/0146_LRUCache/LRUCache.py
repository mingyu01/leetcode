class Node(object):
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.table = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.table:
            node = self.table[key] # table中的键是key，值是一个Node
                                   # Node.key = key, Node.val = val
                                   # Node还有next和prev两个属性
            self._remove(node)
            self._add(node)
            return node.val
        
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.table:
            self._remove(self.table[key])
        node = Node(key, value)
        self.table[key] = node
        self._add(node)
        if len(self.table) > self.capacity:
            first = self.head.next
            self._remove(first)
            del self.table[first.key]
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add(self, node):
        self.tail.prev.next = node
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)