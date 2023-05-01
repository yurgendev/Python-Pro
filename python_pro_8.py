# 3. Напишіть функцію, яка застосує до списку чисел довільну функцію користувача
# і поверне суми елементів отриманого списку.
new_list = [1, 2, 3, 5, 6, 7, 8, 9]


def outer(some_list):
    def inner(num):
        return sum(i ** num for i in new_list)

    return inner


res = outer(new_list)
print(res(3))

# 2. Використовуючи замикання, реалізуйте такий прийом програмування як Мемоізація
# Використовуйте отриманий механізм для прискорення функції рекурсивного обчислення n - го члена ряду Фібоначчі.
# Порівняйте швидкість виконання із просто рекурсивним підходом.
from functools import wraps
from time import perf_counter
import sys


def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]

    return wrapper


@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))

sys.setrecursionlimit(10_000)
start = perf_counter()
f = fibonacci(2000)
end = perf_counter()
print(f)
print(f'time: {end - start} seconds')


# 1. Реалізуйте генераторну функцію, яка повертатиме по одному члену числової послідовності,
# закон якої задається за допомогою функції користувача.

#  Крім цього параметром генераторної функції повинні бути значення першого члена прогресії та кількість членів,
#  що видаються послідовностю.
#  Генератор повинен зупинити свою роботу або по досягненню n-го члена, або при передачі команди на завершення.


def gen_func(first: int, count: int, stop=None):
    current = first
    for _ in range(count):
        if stop is not None and current >= stop + 1:
            return
        yield current
        current = next_item(current)

def next_item(item):
    return item * 2

for item in gen_func(5, 10):
    print(item)
