import threading
import time
from queue import Queue


# Table - класс для столов

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

# Cafe - класс для симуляции процессов в кафе.

class Cafe:
    def __init__(self, tables):
        self.queue = Queue()
        self.tables = tables

# Метод customer_arrival(self) - моделирует приход посетителя(каждую секунду).

    def customer_arrival(self):
        customer_number = 1
        while customer_number <= 20:
            print(f"Посетитель номер {customer_number} прибыл.")
            customer_thread = Customer(customer_number, self)
            customer_thread.start()
            customer_number += 1
            time.sleep(1)

# Метод serve_customer(self, customer) - моделирует обслуживание посетителя.

    def serve_customer(self, customer):
        table_found = False
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель номер {customer.number} сел за стол {table.number}.")
                time.sleep(5)
                table.is_busy = False
                print(f"Посетитель номер {customer.number} покушал и ушёл.")
                table_found = True
                break
        if not table_found:
            print(f"Посетитель номер {customer.number} ожидает свободный стол.")
            self.queue.put(customer)
            self.queue.get()

# Customer - класс (поток) посетителя. Запускается, если есть свободные столы.

class Customer(threading.Thread):
    def __init__(self, number, cafe):
        super().__init__()
        self.number = number
        self.cafe = cafe

    def run(self):
        self.cafe.serve_customer(self)


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

customer_arrival_thread.join()