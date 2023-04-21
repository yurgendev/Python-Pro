# 1. Доповніть клас Група (завдання Лекції 2) можливістю підтримки ітераційного протоколу.





import logging

logger = logging.getLogger('PythonPRO_vol2')
logger.setLevel(logging.INFO)

ch = logging.FileHandler('Student_add_logging')
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch.setFormatter(formatter)

logger.addHandler(ch)

logger.info('adding students to the group')



class MaxStdInGroup(Exception):
    pass


class Human:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Basic example of a human may be presented as a name{self.name}, age{self.age} and its gender{self.gender}"


class Student(Human):

    def __init__(self, name, age, gender, faculty, course):
        super().__init__(name, age, gender)
        self.faculty = faculty
        self.course = course

    def __str__(self):
        return f"Welcome our student - {self.name}. He is {self.age} y.o. and {self.gender} gender. " \
               f"This year student enrolled in {self.faculty} on {self.course} course!"


class Group():

    def __init__(self, students=None, max_students=10):
        if students is None:
            students = []
        self.students = students
        self.max_students = max_students

    def __str__(self):
        return f"This group consists of {len(self.students)} students"

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index >= len(self.students):
            raise StopIteration
        else:
            student = self.students[self.current_index]
            self.current_index += 1
            return student



    def add_student(self, student):
        if len(self.students) <= 10:
            self.students.append(student)
            logger.info(f"Student {student.name} has been added to {student.faculty} on the {student.course} course")
        if len(self.students) > self.max_students:
            raise MaxStdInGroup('there can be no more than 10 students in a group')

    def del_student(self, student):
        if student in self.students:
            self.students.remove(student)
            logger.info(f"Student {student.name} has been deleted")


    def find_student(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def get_student_list(self):
        student_list = ""
        for student in self.students:
            student_list += str(student) + "\n"
        return student_list


# создаем 10 студентов
student1 = Student('Yarik', 28, 'male', 'biofac', 1)
student2 = Student('Vasya', 18, 'male', 'mathfac', 2)
student3 = Student('Mohammed', 38, 'male', 'IT', 3)
student4 = Student('Joe', 20, 'male', 'literature', 4)
student5 = Student('Anastasia', 20, 'female', 'kosmo', 5)
student6 = Student('Olga', 19, 'female', 'biofac', 5)
student7 = Student('Yurik', 23, 'male', 'mathfac', 4)
student8 = Student('Kostian', 24, 'male', 'IT', 3)
student9 = Student('Ronald', 26, 'male', 'biofac', 2)
student10 = Student('Patrik', 28, 'male', 'literature', 1)
student11 = Student('Natasha', 50, 'female', 'math', 3)

# Добавляем/убираем студентов группы
group_1 = Group()

group_1.add_student(student1)
group_1.add_student(student2)
group_1.add_student(student3)
group_1.add_student(student4)
group_1.add_student(student5)
group_1.add_student(student6)
group_1.add_student(student7)
group_1.add_student(student8)
group_1.add_student(student9)
group_1.add_student(student10)
# group_1.add_student(student11)


# group_1.del_student(student1)
# group_1.del_student(student2)

print('*' * 35)
print(group_1)
print()
# список студентов
grp_list = group_1.get_student_list()
print(grp_list)

# проверка есть ли студент в группу
ifStudentInGroup = group_1.find_student('Poroshenko')
print('Student in group' if ifStudentInGroup else 'Student not found')

#
for student in group_1:
    print(student)







