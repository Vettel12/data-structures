"""
Далее Тимофею нужно написать класс MyQueueSized(), который принимает параметр
max_size, означающий максимально допустимое количество элементов в очереди.
Формат ввода
В первой строке записано одно число - количество команд, оно не превосходит 5000. Во
второй строке задан максимально допустимый размер очереди, он не превосходит 5000.
Далее идут команды по одной на строке. Команды могут быть следующих видов:
push x - добавить число x в очередь
pop - удалить число из очереди и вывести на печать
peek - напечатать первое число в очереди
size - вернуть размер очереди
При превышении допустимого размера очереди нужно вывести "error". При вызове операции
pop для пустой очереди нужно вернуть None.
Формат вывода
Напечатайте результаты выполнения нужных команд, по одному на строке.

Ввод
8
2
peek
push 5
push 2
peek
size
size
push 1
size

Выывод
None
5
2
2
error
2

Ввод
10
1
push 1
size
push 3
size
push 1
pop
push 1
pop
push 3
push
3

Вывод
1
error
1
error
1
1
error
"""

class MyQueueSized():
    def __init__(self, m):
        self.queue = [None] * m
        self.max_m = m
        self.head = 0
        self.tail = 0
        self.sizes = 0

    def isEmpty(self):
        return self.sizes == 0
    
    def push(self, item):
        if self.sizes == self.max_m:
            return 'error'
        elif self.sizes != self.max_m:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_m
            self.sizes += 1 

    def pop(self):
        if self.isEmpty == True:
            return None
        else:
            item_pop = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_m
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
        m = int(input())
        if m > 5000:
            raise ValueError
        reuslt = []
        s = MyQueueSized(m)
        for i in range(n):
            commands = input().split()
            if commands[0] == 'push':
                item_push = s.push(commands[1])
                if item_push == 'error':
                    reuslt.append('error')
            elif commands[0] == 'pop':
                item_pop = s.pop()
                if item_pop == None:
                    reuslt.append('None')
                else:
                    reuslt.append(item_pop)
            elif commands[0] == 'peek':
                item_peek = s.peek()
                if item_peek == None:
                    reuslt.append('None')
                else:
                    reuslt.append(item_peek)
            elif commands[0] == 'size':
                item_size = s.size()
                reuslt.append(item_size)
        for i in reuslt:
            print(i)
    except ValueError:
        print('None')

if __name__ == '__main__':
    main()