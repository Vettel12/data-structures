"""
Перед Тимофеем стоит задача написать несколько реализаций собственной очереди, так как
доступные на рынке варианты для проекта не подходят. Требования к первой вот такие: класс
должен называться MyQueue(), поддерживать операции добавления, удаления, получения
элемента, определение текущего размера, и метод, показывающий, пуста ли очередь или нет.
Реализована структура данных должна быть на основе массива.
Формат ввода
В первой строке записано одно число - количество команд, оно не превосходит 5000. Далее
идут команды по одной в строке. Команды могут быть следующих видов:
push x - добавить число x в очередь
роз - удалить число из очереди и напечатать его
peek - напечатать первое число в очереди
size - вернуть размер очереди
Формат вывода
Для каждой команды size, peek и рор напечатайте результат её выполнения. Если очередь
пуста, для команды peek напечатайте None. Если происходит удаление из пустой очереди, то напечатайте None.

Ввод
10
size
push
e
pop
push
2
size
push
-2
pop
push -8
push 4
push 6

Вывод
0
0
1
2

Ввод
10
push 4
pop
push
-1
size
push 0
size
push
-4
size
pop
peek

Вывод
4
1
2
3
-1
0
"""


class MyQueue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.sizes = 0

    def isEmpty(self):
        return self.sizes == 0
    
    def push(self, item):
        if self.sizes != self.max_n:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_n
            self.sizes += 1

    def pop(self):
        if self.isEmpty == True:
            return None
        else:
            item_pop = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_n
            self.sizes -= 1
            return item_pop
        
    def peek(self):
        if self.isEmpty == True:
            return None
        else:
            return self.queue[self.head]
        
    def size(self):
        return self.sizes

def main():
    try:
        n = int(input())
        if n > 5000:
            raise ValueError
        result = []
        s = MyQueue(n)
        for i in range(n):
            commands = input().split()
            if commands[0] == 'push':
                s.push(commands[1])
            elif commands[0] == 'pop':
                item_pop = s.pop()
                if item_pop == None:
                    result.append('None')
                else:
                    result.append(item_pop)
            elif commands[0] == 'peek':
                item_peek = s.peek()
                if item_peek == None:
                    result.append('None')
                else:
                    result.append(item_peek)
            elif commands[0] == 'size':
                item_size = s.size()
                result.append(item_size)
        for i in result:
            print(i)
    except ValueError:
        print('Error')
if __name__ == '__main__':
    main()