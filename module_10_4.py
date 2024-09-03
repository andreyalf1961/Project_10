from random import randint
from threading import Thread
from queue import Queue
from time import sleep

threads = []
class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        pause = randint(3, 10)
        sleep(pause)


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            table_busy = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    threads.append(guest)
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    table_busy = True
                    break
            if not table_busy:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest for table in tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.name} поел(-а) и ушел(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                    if not self.queue.empty():
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        next_guest.start()
                        threads.append(next_guest)
                        print(f'{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол {table.number}')


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

for thread in threads:
    thread.join()
