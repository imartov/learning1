from multiprocessing import Pipe, Process
import multiprocessing
import time


def getter(pipe):
    out, inp = pipe
    inp.close() # закрываем переменную, которая служит для передачи данных
                # процесс сможет только читать данные
    while True:
        try:
            print("data: ", out.recv()) # после отправки данных в функции setter данный метод разблокируется и выведет все на экран и перейдет на след. итерацию цикла
        except:
            break


def setter(sequence, inpute_c):
    for item in sequence:
        time.sleep(1)
        inpute_c.send(item) # отправляем последовательность данных во входящий канал
    

if __name__ == '__main__':
    outpute_c, inpute_c = Pipe()
    g = multiprocessing.Process(target=getter, args=((outpute_c, inpute_c), )) # создание отдельного процесса
    g.start()
    outpute_c.close() # закрываем переменную в основном процессе
    
    setter([1, 2, 3, 4, 5], inpute_c)
    inpute_c.close()
    g.join() # дожидаемся выполнения основного процесса