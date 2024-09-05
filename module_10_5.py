import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            all_data.append(line)


if __name__ == '__main__':
    filenames = [f'text{number}.txt' for number in range(1, 5)]
    # Линейный вызов
    start = datetime.datetime.now()
    for filename in filenames:
        read_info(filename)
    end = datetime.datetime.now()
    print(f'{end - start} (линейный)')

    # Многопроцессный вызов
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(f'{end - start} (многопроцессный)')
