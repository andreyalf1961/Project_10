import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(10):
            bal = randint(50, 500)
            self.balance += bal
            print(f'Пополнение i={i}: {bal}, Баланс: {self.balance}\n')
            if self.balance >= 0 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(10):
            bal = randint(50, 500)
            print(f'Запрос i={i} на {bal}\n')
            if bal <= self.balance:
                self.balance -= bal
                print(f'Снятие: {bal}, Баланс: {self.balance}\n')
                sleep(0.001)
            else:
                print(f'Запрос отклонён, недостаточно средств\n')
                self.lock.acquire()
                sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
