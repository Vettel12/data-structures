"""
Любимый вариант очереди Тимофея - очередь, написанная с использованием связного
списка. Помогите ему с реализацией. Очередь должна поддерживать методы get, put, size.
Формат ввода
В
первой строке записано количество команд n - целое число, не превосходящее 1000. В
каждой из следующих n строк записана команда: get, put, или size.
Формат вывода
При вызове метода get напечатайте возвращаемое значение. Если метод get вызывается у
пустой очереди, нужно напечатать 'error'. При вызове метода size - вывести размер очереди.

Пример 1
Ввод
10
put -34
put -23
get
size
get
size
get
get
put 80
size

Вывод
2
2
-66
98

Ввод
6
put -66
put 98
size
size
get
get

Вывод
2
2
-66
98

Ввод
get
size
put 74
get
size
put 90
size
size
size

Вывод
error
0
74
0
1
1
1
"""

class Node:
    def __init__(self, value = None, next_item = None):
        self.value = value
        self.next_item = next_item

class Queue:
    def __init__(self, n):
        self.head = 0
        self.tail = 0
        self.max_n = n
        self.sizes = 0

    def isEmpty(self):
        return self.sizes == 0
    
    def put(self, value):
        if self.sizes != self.max_n:
            new_node = Node(value)
            if self.isEmpty() == True:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next_item = new_node
                self.tail = new_node
            self.sizes += 1
    
    def get(self):
        if self.isEmpty():
            return 'error'
        else:
            item_get = self.head.value
            self.head = self.head.next_item
            self.sizes -= 1
            return item_get
        
    def size(self):
        return self.sizes

def main():
    try:
        n = int(input())
        if n > 1000:
            raise ValueError
        s = Queue(n)
        result = []
        for x in range(n):
            commands = input().split()
            if commands[0] == 'get':
                item_get = s.get()
                if item_get == 'error':
                    result.append('error')
                else:
                    result.append(item_get)
            elif commands[0] == 'put':
                s.put(commands[1])
            elif commands[0] == 'size':
                item_size = s.size()
                result.append(item_size)
        for i in result:
            print(i)
    except ValueError:
        print('error')

if __name__ == '__main__':
    main()