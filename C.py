"""
На вход подается строка. Нужно определить длину наибольшей подстроки, которая не
содержит повторяющиеся символы.
Формат ввода
Одна строка, состоящая из латинских букв. Длина строки не превосходит 10000.
Формат вывода
Одно число - ответ на задачу.

Пример 1

Ввод
abcabcb

Вывод
3

Пример 2

Ввод
bbbbb

Вывод
1

"""

# Реализая получилась по памяти O(min(m, n)), а по времени O(n)

def max_str(string):
    str_dict = {}
    left = 0
    right = 0
    maximum = 0

    while right < len(string):
        if string[right] in str_dict:
            left = str_dict[string[right]] + 1
        str_dict[string[right]] = right
        maximum = max(maximum, right - left + 1)
        right += 1

    return maximum


def main():
    try:
        string = input()
        if len(string) > 10000:
            raise ValueError
        
        print(max_str(string))
        
    except ValueError:
        print("Invalid input")

if __name__ == '__main__':
    main()