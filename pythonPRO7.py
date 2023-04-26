# 1. Реалізуйте генераторну функцію, яка повертатиме по одному члену геометричної прогресії
# із зазначеним множником.

#  Генератор повинен зупинити свою роботу або після досягнення зазначеного елементу,
#  або при передачі команди на завершення.


def geometric(start, mn, stop=None):
    while stop is None or start <= stop:
        try:
            yield start
            start *= mn
        except GeneratorExit:
            return
    raise StopIteration



gp = geometric(1, 2, stop=5000)

for i in gp:
    print(i)


# 2. Реалізуйте свій аналог генераторної функції range().

def new_range(start, stop, step):
    if (start >= stop and step > 0) or step == 0:
        raise ValueError("incorrect input")
    while start < stop:
        yield start
        start += step


res = new_range(0, 10, 2)
for i in res:
    print(i)


# 3. Напишіть функцію-генератор, яка повертатиме прості числа.
# Верхня межа діапазону повинна бути задана параметром цієї функції.

def prime(limit):
    for x in range(2, limit + 1):
        is_prime = True
        for d in range(2, int(x ** 0.5) + 1):
            if x % d == 0:
                is_prime = False
                break
        if is_prime:
            yield x


for nums in prime(15):
    print(nums)


# 4. Напишіть генераторний вираз для заповнення списку.
# Список повинен бути заповнений кубами чисел від 2 до вказаної вами величини.
range_limit = 10
generator_list = [x ** 3 for x in range(range_limit)]
print(generator_list)

