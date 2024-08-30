import time
from time import sleep
from threading import Thread

import os


def write_words(word_count, file_name):
    open(file_name, 'w').close()
    for i in range(1, word_count + 1):
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f"Какое-то слово №{i}\n")
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


time_st = time.time()
res = write_words(10, 'example1.txt')
res = write_words(30, 'example2.txt')
res = write_words(200, 'example3.txt')
res = write_words(100, 'example4.txt')
time_en = time.time()
time_del = time_en - time_st
print(f'работа функций {time_del} сек')


time_st = time.time()
thr_f = Thread(target=write_words, args=(10, 'example.5txt'))
thr_s = Thread(target=write_words, args=(30, 'example.6txt'))
thr_t = Thread(target=write_words, args=(200, 'example.7txt'))
thr_fr = Thread(target=write_words, args=(100, 'example.8txt'))

thr_f.start()
thr_s.start()
thr_t.start()
thr_fr.start()

thr_f.join()
thr_s.join()
thr_t.join()
thr_fr.join()

time_en = time.time()
time_del = time_en - time_st
print(f'работа потоков {time_del} сек')
