"""
Вася решил запутать маму – делать дела в обратном порядке. Список его дел теперь хранится в двусвязном списке. 
Напишите функцию, которая вернёт список в обратном порядке.

Внимание: в этой задаче не нужно считывать входные данные. 
Нужно написать только функцию, которая принимает на вход голову двусвязного списка и возвращает голову перевёрнутого списка. 
Ниже дано описание структуры, которая задаёт вершину списка.

Формат ввода

Функция принимает на вход единственный аргумент — голову двусвязного списка.

Длина списка не превосходит 1000 элементов. Список не бывает пустым.

Формат вывода

Функция должна вернуть голову развернутого списка.
"""

class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None) -> None:
        self.value = value
        self.next = next
        self.prev = prev

    def solution(self):
        current_node = self
        count = current_node.next
        current_node.prev = current_node.next
        current_node.next = None
        while count is not None:
            count.prev = count.next
            count.next = current_node
            current_node = count
            count = count.prev
        return current_node
        

# Шаг 1: Создайте узлы с их значениями, первоначально с параметрами next и prev, установленными на None.
a = DoubleConnectedNode("A")
b = DoubleConnectedNode("B")
c = DoubleConnectedNode("C")
d = DoubleConnectedNode("D")
e = DoubleConnectedNode("E")

# Шаг 2: Свяжите узлы соответствующим образом
a.next = b

b.next = c
b.prev = a

c.next = d
c.prev = b

d.next = e
d.prev = c

e.prev = d

reversed_head = DoubleConnectedNode.solution(a)

current_node = reversed_head
while current_node:
    print(current_node.value)
    current_node = current_node.next