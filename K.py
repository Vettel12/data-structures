"""
Реализуйте класс StackSet, который хранит только уникальные элементы. При этом операция
добавления элемента в стек должна выполняться за O(1).
Формат ввода
В первой строке записано одно число - количество команд. Далее идут команды по одной на
строке. Команды могут быть следующих видов:
push x - добавить число х в
стек
рор - удалить число с вершины стека
peek - напечатать число с вершины стека (без удаления)
size - узнать размер стека
Если стек пуст при вызове команд роз и реек нужно вывести на печать error.
Формат вывода
Для каждой команды size напечатайте результат её выполнения. Если происходит удаление из
пустого стека - напечатайте error.

Ввод
8
push 1
push 2
size
push 2
size
pop
push 1
size

Вывод
2
2
1

Ввод
10
push 1
pop
push
2
size
push
1
push 2
pop
push
2
peek
pop

Вывод
1
2

"""

class StackSet:
    def __init__(self):
        self.items = []
        self.unique_items = set()

    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.unique_items.add(item)
        if self.isEmpty():
            self.items.append(item)
        elif len(self.unique_items) > len(self.items):
            self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return 'error'
        else:
            self.unique_items.remove(self.items[-1])
            return self.items.pop()
        
    def peek(self):
        if self.isEmpty():
            return 'error'
        else:
            return self.items[len(self.items)-1]
    
    def size(self):
        if self.isEmpty():
            return 'error'
        else:
            return len(self.items)
        

def main():
    n = int(input())
    s = StackSet()
    result = []
    for i in range(n):
        commands = input().split()
        if commands[0] == 'push':
            s.push(commands[1])
        elif commands[0] == 'pop':
            deleted_item = s.pop()
            if deleted_item == "error":
                result.append(deleted_item)
        elif commands[0] == 'peek':
            peek_item = s.peek()
            result.append(peek_item)
        else:
            size_item = s.size()
            result.append(size_item)
    for x in result:
        print(x)

if __name__ == '__main__':
    main()