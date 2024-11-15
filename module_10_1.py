# import time
# from time import sleep
# import threading

# def write_words(word_count, file_name):
#     with open(file_name, 'w', encoding='utf-8') as f:
#         for i in range(1, word_count + 1):
#             f.write(f"Какое-то слово № {i}\n")
#             sleep(0.1)  # Задержка 0.1 секунды
#             start_time = time.time()
#             end_time = time.time()
#             elapsed_time = end_time - start_time
#             # elapsed_time = time.localtime()
#
#             print(f'Работа потоков', elapsed_time)
#
#
#             #print(f' Работа потоков {time.ctime()}')
#     print(f"Завершилась запись в файл {file_name}")


# write_words(10, 'example1.txt')
# write_words(30, 'example2.txt')
# write_words(200, 'example3.txt')
# write_words(100, 'example4.txt')
# thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
# thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
# thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
# thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
# thread1.start()
# thread1.join()
# thread2.start()
# thread3.start()
# thread4.start()
import time
from time import sleep
import threading

# Глобальная блокировка для синхронизации потоков
lock = threading.Lock()

def write_words(word_count, file_name):
    start_time = time.time()  # Начало отсчета времени
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            with lock:  # Используем блокировку при записи в файл
                f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)  # Задержка 0.1 секунды

    end_time = time.time()  # Конец отсчета времени
    elapsed_time = end_time - start_time
    print(f"Завершилась запись в файл {file_name}.")
    print(f"Время выполнения: {elapsed_time} секунд.")

# Запуск функций записи в файлы в отдельных потоках
threads = []
file_configs = [(10, 'example1.txt'), (30, 'example2.txt'), (200, 'example3.txt'), (100, 'example4.txt')]

for word_count, file_name in file_configs:
    thread = threading.Thread(target=write_words, args=(word_count, file_name))
    threads.append(thread)
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()
