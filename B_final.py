class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.value)
    
    def hasCycle(self):
        slow = self
        fast = self
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
g = Node("воскресенье", None)
f = Node("суббота", g)
e = Node("пятница", f)
d = Node("четверг", e)
c = Node("среда", d)
b = Node("вторник", c)
a = Node("понедельник", b)

e.next = a

print(a.hasCycle())