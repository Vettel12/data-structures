"""
Гоша решил реализовать структуру данных Дек, максимальный размер которого определяется
заданным числом. Методы push_back, push_front, pop_front, pop_back работали корректно. Ho
если в деке было много элементов, программа работала очень долго. Дело в том, что не все
операции выполнялись за О(1). Помогите Гоше! Напишите эффективную реализацию.
Формат ввода
В первой строке записано количество команд п - целое число, не превосходящее 5000. Во
второй строке записано число m - максимальный размер дека. Он не превосходит 1000. В
следующих п строках записана одна из команд:
push_back value
push front value
pop_front
pop back
value - целое число, по модулю не превосходящее 1000.
Формат вывода
При вызове команд pop_front и pop_back нужно вывести возвращаемое значение. Если они
вызываются для пустого дека - напечатайте 'error'. Если команда push_back или push_front
вызывается для дека, размер которого равен максимально возможному, тоже нужно вывести
'error'.

Ввод
4
4
push_front 861
push_front -819
pop_back
pop_back

Вывод
861
-819

Ввод
7
10
push_front -855
push_front 720
pop_back
pop_back
push_back 844
pop_back
push_back 823

Вывод
-855
720
844

Ввод
6
6
push_front -201
push_back 959
push_back 102
push_front 20
pop_front
pop_back

Вывод
20
102

"""

class Deque:
    def __init__(self, m):
        self.queue = [None] * m
        self.max_m = m
        self.head = 0
        self.tail = 0
        self.sizes = 0

    def isEmpty(self):
        return self.sizes == 0
    
    def push_back(self, item):
        if self.sizes == self.max_m:
            return 'error'
        else:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_m
            self.sizes += 1

    def push_front(self, item):
        if self.sizes == self.max_m:
            return 'error'
        else:
            self.head = (self.head - 1) % self.max_m
            self.queue[self.head] = item
            self.sizes += 1

    def pop_back(self):
        if self.isEmpty == True:
            return 'error'
        else:
            self.tail = (self.tail - 1) % self.max_m
            item_pop_back = self.queue[self.tail]
            self.queue[self.tail] = None
            self.sizes -= 1
            return item_pop_back
        
    def pop_front(self):
        if self.isEmpty(): 
            return 'error'
        else:
            item_pop_front = self.queue[self.head] 
            self.queue[self.head] = None  
            self.head = (self.head + 1) % self.max_m 
            self.sizes -= 1
            return item_pop_front


def main():
    try:
        n = int(input())
        if n > 5000:
            raise ValueError
        m = int(input())
        if m > 1000:
            raise ValueError
        s = Deque(m)
        result = []
        for x in range(n):
            commands = input().split()
            if commands[0] == 'push_back':
                if abs(int(commands[1])) > 1000:
                    result.append('error')
                else:
                    item_push_back = s.push_back(commands[1])
                    if item_push_back == 'error':
                        result.append(item_push_back)
            elif commands[0] == 'push_front':
                if abs(int(commands[1]))> 1000:
                    result.append('error')
                else:
                    item_push_front = s.push_front(commands[1])
                    if item_push_front == 'error':
                        result.append(item_push_front)
            elif commands[0] == 'pop_back':
                item_pop_back = s.pop_back()
                if item_pop_back == 'error':
                    result.append('error')
                else:
                    result.append(item_pop_back)
            elif commands[0] == 'pop_front':
                item_pop_front = s.pop_front()
                if item_pop_front == 'error':
                    result.append('error')
                else:
                    result.append(item_pop_front)
        for i in result:
            print(i)
    except ValueError:
        print('None')
        
if __name__ == '__main__':
    main()