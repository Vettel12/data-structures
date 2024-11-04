"""
Алла реализовывала алгоритм шифрования и что-то напутала. В итоге после расшифровки
буквы в словах получились в произвольном порядке. Помогите Алле разобраться с
проблемой. Напишите функцию, принимающую на вход строку и шаблон и определяющую,
сколько анаграмм шаблона будет в строке.
Напомним, что два слова - анаграммы, если одно из них можно получить из другого,
переставив буквы. Например, слова «кот» и «ток».
Формат ввода
В первой строке задана строка, в которой будет производиться поиск. Во второй - шаблон.
Длина обеих строк не превосходит 1000 и длина шаблона не может быть больше длины
строки для поиска.
Формат вывода
Одно число - ответ на задачу.

Ввод
cba
abc

Вывод
1

Ввод
abcsdfacba
abc

Вывод
3
"""
class CountAnagrams:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.count = 0
        self.queue = []

    def count_anagrams(self):
        len_s1 = len(self.str1)
        len_s2 = len(self.str2)

        # Функция для создания словаря подсчета символов
        def create_char_count(s):
            char_count = {}
            for char in s:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
            return char_count

        # Счетчик символов шаблона
        pattern_counter = create_char_count(self.str2)
        # Счетчик символов текущего окна в строке
        window_counter = {}

        # Инициализация окна и счетчика для первых len_s2 символов
        for i in range(len_s2):
            self.queue.append(self.str1[i])
            if self.str1[i] in window_counter:
                window_counter[self.str1[i]] += 1
            else:
                window_counter[self.str1[i]] = 1

        # Проверка, является ли начальное окно анаграммой
        if window_counter == pattern_counter:
            self.count += 1

        # Скользим окно по строке
        for i in range(len_s2, len_s1):
            # Удаляем символ, который выходит из окна
            left_char = self.queue.pop(0)
            if window_counter[left_char] == 1:
                del window_counter[left_char]
            else:
                window_counter[left_char] -= 1

            # Добавляем новый символ, который входит в окно
            new_char = self.str1[i]
            self.queue.append(new_char)
            if new_char in window_counter:
                window_counter[new_char] += 1
            else:
                window_counter[new_char] = 1

            # Проверяем, является ли текущее окно анаграммой
            if window_counter == pattern_counter:
                self.count += 1

        return self.count

def main():
    try:
        str1 = input().strip()
        if len(str1) > 1000:
            raise ValueError("Длина строки превышает допустимый лимит.")
        
        str2 = input().strip()
        if len(str2) > 1000 or len(str2) > len(str1):
            raise ValueError("Недопустимая длина шаблона.")
        
        count_anagrams = CountAnagrams(str1, str2)
        print(count_anagrams.count_anagrams())
    except ValueError as e:
        print("error:", e)

if __name__ == '__main__':
    main()