# 1) Создайте декоратор, который будет подсчитывать, сколько раз была вызвана декорируемая функция.


def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


@counter
def my_func():
    return 'Hello, world'


my_func()
my_func()
my_func()

print(my_func.calls)

# Создайте декоратор, который зарегистрирует декорируемую функцию в списке функций,
# для обработки последовательности.

functions_list = []


def func_registrator(func):
    functions_list.append(func)
    return func_registrator


@func_registrator
def any_func_1():
    return 'Test func1'


@func_registrator
def any_func_2():
    return 'Test func2'


@func_registrator
def any_func_3():
    return 'Test func3'


@func_registrator
def any_func_4():
    return 'Test func4'


for f in functions_list:
    print(f())


# 3) Предположим, в классе определен метод _str., который возвращает
# строку на основании класса. Создайте такой декоратор для этого метода, чтобы полученная строка сохранялась
# в текстовый файл, имя которого совпадает с именем класса, метод которого вы декорировали.


def save_file(cls):
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        res = instance.__str__()
        filename = f'{instance.__class__.__name__}.txt'
        with open(filename, "w") as f:
            f.write(res)
        return res

    return wrapper


@save_file
class Homework:

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f'test text {self.text}'


result = Homework('abc')
print(result)

# 4) Создайте декоратор с параметрами для проведения хронометража работы той или иной функции.
# Параметрами должны выступать то, сколько раз нужно запустить декорируемую функцию и в какой файл сохранить
# результаты хронометража. Цель - провести хронометраж декорируемой функции.

from datetime import datetime


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        res = func(*args, **kwargs)
        end_time = datetime.now()

        print(f"function execution time {func.__name__}: {(end_time - start_time).total_seconds()} sec")
        return res
    return wrapper


@timer
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


print(fibo(25))

# Создайте декоратор, который зарегистрирует декорируемый класс в списке классов.

classes_list = []


def class_to_list(cls):
    classes_list.append(cls)
    return cls


@class_to_list
class First_class:
    pass


@class_to_list
class Second_class:
    pass


print(classes_list)


# Создайте декоратор класса с параметром. Параметром должна быть строка, которая должна дописываться (слева)
# к результату работы метода __str__

def text_decorator(any_text):
    def wrapper(cls):
        original_text = cls.__str__

        def __str__(self):
            return any_text + original_text(self)
        cls.__str__ = __str__
        return cls
    return wrapper

@text_decorator("new text")
class Texting:
    def __str__(self):
        return ' <-- this text was added'

res = Texting()
print(res)


# Для класса Вох напишите статистический метод, который будет подсчитывать суммарный объем двух ящиков,
# которые будут его параметрами.


class Box:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        return self.x * self.y * self.z

    @staticmethod
    def total_volume(box1, box2):
        return box1.volume() + box2.volume()


box_1 = Box(2, 3, 5)
box_2 = Box(4, 5, 2)

res1 = Box.total_volume(box_1, box_2)
print(res1)
