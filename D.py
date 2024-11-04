"""
Дана матрица. Нужно написать функцию, которая для элемента возвращает всех его соседей. 
Соседним считается элемент, находящийся от текущего на одну ячейку влево, вправо, вверх или вниз. 
Диагональные элементы соседними не считаются.

Формат ввода

В первой строке задано n — количество строк матрицы. 
Во второй — количество столбцов m. Числа m и n не превосходят 1000. 
В следующих n строках задана матрица. Элементы матрицы — целые числа, по модулю не превосходящие 1000. 
В последних двух строках записаны координаты элемента (индексация начинается с нуля), соседей которого нужно найти.

Формат вывода

Напечатайте нужные числа в возрастающем порядке через пробел.

4
3
1 2 3
0 2 6
7 4 1
2 7 0
3
0
[7, 7]

4
3
1 2 3
0 2 6
7 4 1
2 7 0
0
0
[0, 2]
"""

# Реализация получилась по памяти O(1) так как макс. 4 элемента, а по времени O(1) так макс. 4 элемента


def  num_s(n, m, matrix, x, y):
    result = []
    if x > 0:
        result.append(matrix[x-1][y])
    if x < n-1:
        result.append(matrix[x+1][y])
    if y > 0:
        result.append(matrix[x][y-1])
    if y < m-1:
        result.append(matrix[x][y+1])
    return sorted(result)

def main():
    try:
        n = int(input())
        m = int(input())
        if  n > 1000 or m > 1000:
            raise ValueError
        matrix = []
        for x in range(n):
            row = list(map(int, input().split()))
            for num in row:
                if abs(num) > 1000:
                    raise ValueError
            matrix.append(row)
        x = int(input())
        y = int(input())
        print(" ".join(map(str,num_s(n, m, matrix, x, y))))
    except ValueError:
        print("Invalid input")

if __name__ == '__main__':
    main()