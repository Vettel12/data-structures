"""
Нужно реализовать класс Stack Max, который поддерживает операцию определения
максимума среди всех элементов в стеке. Класс также должен поддерживать все операции,
реализованные в классе Stack, из урока. При этом в классе Stack Max может быть реализовано
не более трёх методов.
Стек может содержать только данные типов, поддерживающих операцию сравнения. Иначе
операция поиска максимума будет некорректной.
Формат ввода
В первой строке записано одно число n - количество команд. n не превосходит 1000. В
следующих п строках идут команды. Команды могут быть следующих видов:
push x - добавить число х в стек
рор - удалить число с вершины стека
get_max - напечатать максимальное число в стеке
Если стек пуст при вызове команды get_max нужно напечатать None, для команды
pop - error.
Формат вывода
Для каждой команды get_max напечатайте результат её выполнения. Если стек пустой, для
команды get_max напечатайте None. Если происходит удаление из пустого стека - напечатайте
error.

Ввод
8
get_max
push
7
pop
push -2
push -1
рop
get_max
get_max

Вывод
None
-2
-2

Ввод
7
get_max
dod
dod
dod
push 10
get_max
push -9

Вывод
None
error
error
error
10
"""

class Stack:
    def __init__ (self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return 'error'
        else:
            return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    
    def get_max(self):
        if self.isEmpty():
            return None
        else:
            max_value = self.items[0]
            for i in self.items:
                if i > max_value:
                    max_value = i
            return max_value

def main():
    try:
        n = int(input())
        if n > 1000:
            raise ValueError
        s = Stack()
        result = []
        for x in range(n):
            comamnds = input().split()
            if comamnds[0] == 'push':
                s.push(comamnds[1])
            if comamnds[0] == 'pop':
                popped_item = s.pop()
                if popped_item == 'error':
                    result.append(popped_item)
            if comamnds[0] == 'get_max':
                max_item =s.get_max()
                result.append(max_item)
        for x in result:
            print(x)
    except ValueError:
        print("Invalid input")

if __name__ == '__main__':
    main()