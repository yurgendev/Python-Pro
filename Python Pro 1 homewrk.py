# 1. Створіть клас для опису товару. У якості атрибутів товару можете використовувати значення ціни товару,
# опису товару, габарити товару. Створіть пару екземплярів вашого класу та протестуйте їхню роботу.


class Cars:
    def __init__(self, price, description, type):
        self.price = price
        self.description = description
        self.type = type

    def __str__(self):
        return f"This is a {self.description}, equipment here is: {self.type} and price is {self.price}"



# 2. Створіть клас "Покупець". У якості атрибутів можна використовувати
# прізвище, ім'я, по батькові, мобільний телефон тощо.

class Customer:
    def __init__(self, name, surname, number, delivery_address):
        self.name = name
        self.surname = surname
        self.number = number
        self.delivery_address = delivery_address

    def __str__(self):
        return f"Customer name: {self.name}, {self.surname}, {self.number}, \n{self.delivery_address}."




# 3. Створіть клас "Замовлення". Замовлення може містити декілька товарів певної кількості.
# Замовлення має містити дані про користувача, який його здійснив. Реалізуйте метод обчислення сумарної
# вартості замовлення. Визначте метод str() для коректного виведення інформації про це замовлення.


class Order:
    def __init__(self, car, customer):
            self.car = car
            self.customer = customer
            self.total_price = car.price

    def __str__(self):
        return f"Order info: \n{self.car}, \n{self.customer}, \nTotal price: {self.total_price}"

    def add_item(self, *cars):
        for car in cars:
            self.total_price += car.price



car1 = Cars(12500, 'Mercedes Benz C300', 'Cabrio')
customer1 = Customer('Stepan', 'Bandera', '+380970000001', 'Ukraine: Lviv, str. tra-la-la, 28')
order1 = Order(car1, customer1)

car2 = Cars(10000, 'BMW 528i', 'Sedan')
car3 = Cars(50000, 'BMW 730', 'Sedan')
customer2 = Customer('Isaak', 'Avraamovich', '+380970000002', 'Israel: Petakh-Tikva, str. ola-la, 1/2')
order2 = Order(car2, customer2)

print(order1)
print()
print(order2)

order2.add_item(car2, car3)

print(f'if Customer buys both cars it costs: {order2.total_price}')






