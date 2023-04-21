# 2. Модифікуєте клас Замовлення (завдання Лекції 1),
# додавши реалізацію протоколу послідовностей та ітераційного протоколу.


class Cars:
    def __init__(self, price, description, type):
        self.price = price
        self.description = description
        self.type = type

    def __str__(self):
        return f"This is a {self.description}, equipment here is: {self.type} and price is {self.price}"


class Customer:
    def __init__(self, name, surname, number, delivery_address):
        self.name = name
        self.surname = surname
        self.number = number
        self.delivery_address = delivery_address

    def __str__(self):
        return f"Customer name: {self.name}, {self.surname}, {self.number}, \n{self.delivery_address}."


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = {}

    #      протокол последовательности для длинны заказа (в данном случае покажет кол-во уникальных машин в заказе)
    # def __len__(self):
    #     return len(self.items)

    # И поскольку в задаче не уточняется как именно должен работать метод len предлагаю оба варианта

    #      либо можно вывести длинну заказа в виде общего количества машин в заказе
    def __len__(self):
        total_quantity = 0
        for quantity in self.items.values():
            total_quantity += quantity
        return total_quantity

    # при вызове индекса в заказе мы получаем конкретный автомобиль в заказе который подвязан под его индекс
    def __getitem__(self, index):
        keys = list(self.items.keys())
        if isinstance(index, int):
            item = keys[index]
            return f"{item.description} x {self.items[item]}"
        else:
            raise TypeError("incorrect index data")


    # итерационный протокол
    def __iter__(self):
        self._index = 0
        self._items = list(self.items.items())
        return self

    def __next__(self):
        if self._index >= len(self._items):
            raise StopIteration
        item, quantity = self._items[self._index]
        self._index += 1
        return (item, quantity)



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
        items_str = "\n".join(
            [f"{item.description} x {quantity} - {item.price * quantity}$" for item, quantity in self.items.items()])
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
print('*' * 50)
print(customer2)

# проверка протокола последовательности и итератора
print(len(order))
print(order[2])
for item, quantity in order:
    print(item, quantity)
