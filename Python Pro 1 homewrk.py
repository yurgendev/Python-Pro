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
    def __init__(self, customer):
        self.customer = customer
        self.items = {}

    def add_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def get_total_price(self):
        total_price = 0
        for item, quantity in self.items.items():
            total_price += item.price * quantity
        return total_price

    def __str__(self):
        items_str = "\n".join([f"{item.description} x {quantity} - {item.price*quantity}$" for item, quantity in self.items.items()])
        return f"Order by {self.customer.name} {self.customer.surname}:\n{items_str}\nTotal price: {self.get_total_price()}$"



car1 = Cars(12500, 'Mercedes Benz C300', 'Cabrio')
car2 = Cars(10000, 'BMW 528i', 'Sedan')
car3 = Cars(50000, 'BMW 730', 'Sedan')
car4 = Cars(250_000, 'Urus', 'SUV')

customer1 = Customer('Stepan', 'Bandera', '+380970000001', 'Ukraine: Lviv, str. tra-la-la, 28')
customer2 = Customer('Isaak', 'Avraamovich', '+380970000002', 'Israel: Petakh-Tikva, str. ola-la, 1/2')





order = Order(customer2)
order.add_item(car1, 1)
order.add_item(car2, 2)
order.add_item(car3, 3)
order.add_item(car4, 1)
print(order)
print('*'* 50)
print(customer2)




