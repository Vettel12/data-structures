"""
Напишите код для решения задачи про поиск кружков, которые посещает хотя бы один ученик
Ваше решение должно задействовать О(1) дополнительной памяти (то есть помимо памяти,
выделенной под массив visited_optional_courses)
Формат ввода
В первой строке записано количество кружков п, целое число, не превосходящее 10000 В
следующих и строках записаны названия кружков.
Формат вывода
Выведите уникальные названия кружков по одному на строке, в порядке появления во
входных данных.

Пример

Ввод
8
вышивание крестиком
рисование мелками на парте
настольный керлинг
настольный керлинг
кухня африканского племени ужасной
тяжелая атлетика
таракановедение
таракановедение

Вывод
вышивание крестиком
рисование мелками на парте
настольный керлинг
кухня африканского племени ужасной
тяжелая атлетика
таракановедение
"""
# Реализация получилась по памяти O(1), а по времени O(n)

def circle(n, visited_optional_courses):
    [print(x) for x in visited_optional_courses.keys()]

def main():
    try:
        n = int(input())
        if n>10000 or n<1:
            raise ValueError
        visited_optional_courses = {}
        for x in range(n):
            sentence = input()
            if sentence not in visited_optional_courses:
                visited_optional_courses[sentence] = 1
            else:
                visited_optional_courses[sentence] += 1
        circle(n, visited_optional_courses)
    except ValueError:
        print("Invalid input")
    
if __name__ == '__main__':
    main()