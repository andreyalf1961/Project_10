import time
from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        v = 100
        d = 0
        while v > 0:
            time.sleep(1)
            v -= self.power
            d += 1
            print(f'{self.name} сражается {d} дней(дня)..., осталось {v} воинов.\n')
        print(f'{self.name} одержал победу спустя {d} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print(f'Все битвы закончились!')
