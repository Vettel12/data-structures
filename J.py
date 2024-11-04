"""
Реализуйте класс StackMaxEffective, поддерживающий операцию определения максимума среди элементов в стеке. 
Сложность операции должна быть O(1). Для пустого стека операция должна возвращать None. 
При этом push(x) и pop() также должны выполняться за константное время.

Формат ввода

В первой строке записано одно число — количество команд, оно не превосходит 100000. 
Далее идут команды по одной в строке. Команды могут быть следующих видов:

push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;

Если стек пуст, при вызове команды get_max нужно напечатать «None», для команды pop — «error».

Формат вывода

Для каждой команды get_max() напечатайте результат её выполнения. Если стек пустой, 
для команды get_max() напечатайте «None». Если происходит удаление из пустого стека — напечатайте «error».

Ввод
10
pop
pop
push 4
push -5
push 7
pop
pop
get_max
pop
get_max

Вывод
error
error
4
None

Ввод
10
get_max
push -6
dod
dod
get_max
push 2
get_max
dod
push -2
push -6

Вывод
None
error
None
2
"""

class StackMaxEffective:
    def __init__ (self):
        self.items = []
        self.max_stack = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        if len(self.max_stack) == 0:
            self.max_stack.append(item)
        elif item >= self.max_stack[-1]:
            self.max_stack.append(item)

    def pop(self):
        if self.isEmpty():
            return 'error'
        else:
            popped_item = self.items.pop()
            if popped_item == self.max_stack[-1]:
                self.max_stack.pop()
            return popped_item

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    
    def get_max(self):
        if self.isEmpty():
            return None
        else:
            return self.max_stack[-1]


def main():
    try:
        n = int(input())
        if n > 100000:
            raise ValueError
        s = StackMaxEffective()
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