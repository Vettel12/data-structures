"""
Вася размышляет, что ему можно не делать из того списка дел, который он составил. Но, кажется, 
все пункты очень важные! Вася решает загадать число и удалить дело, которое идёт под этим номером. 
Список дел представлен в виде односвязного списка. Напишите функцию solution, которая принимает 
на вход голову списка и номер удаляемого дела и возвращает голову обновлённого списка.

Формат ввода

Функция принимает голову списка и индекс элемента, который надо удалить (нумерация с нуля). 
Список содержит не более 5000 элементов. Список не бывает пустым.      

Формат вывода

Верните голову списка, в котором удален нужный элемент.


"""

class Node:
    def __init__(self, value, next_item=None) -> None:
        self.value = value
        self.next_item = next_item

    def solution(self, idx):
        current_node = self
        previous_node = None
        if idx == 1:
            return self.next_item
        while idx > 1:
            previous_node = current_node
            current_node = current_node.next_item
            idx -= 1
        if previous_node:
            previous_node.next_item = current_node.next_item
        return self

e = Node(5, None)
d = Node(4, e)
c = Node(3, d)
b = Node(2, c)
a = Node(1, b)

idx = 5

head = a.solution(idx)

while head:
    print(head.value)
    head = head.next_item