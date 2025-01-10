
import time
from time import sleep
import threading

# Глобальная блокировка для синхронизации потоков
lock = threading.Lock()

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            with lock:  # Используем блокировку при записи в файл
                f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)  # Задержка 0.1 секунды
    print(f"Завершилась запись в файл {file_name}")

# Запуск функций записи в файлы в отдельных потоках
threads = []
file_configs = [(10, 'example1.txt'), (30, 'example2.txt'), (200, 'example3.txt'), (100, 'example4.txt')]

# Измерение времени выполнения первых четырех файлов
start_time = time.time()

for word_count, file_name in file_configs:
    thread = threading.Thread(target=write_words, args=(word_count, file_name))
    threads.append(thread)
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

end_time = time.time()
print(f"Работа функций заняла: {end_time - start_time:.2f} секунд.")

# Создание и запуск потоков для дополнительных файлов
additional_file_configs = [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]
threads = []

start_time_threads = time.time()  # Начало отсчета времени для потоков

for word_count, file_name in additional_file_configs:
    thread = threading.Thread(target=write_words, args=(word_count, file_name))
    threads.append(thread)
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

end_time_threads = time.time()  # Конец отсчета времени для потоков
print(f"Работа потоков заняла: {end_time_threads - start_time_threads:.2f} секунд.")
