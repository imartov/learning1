# client.py
from multiprocessing.managers import BaseManager


BaseManager.register("get") # регистрируем функцию
manager = BaseManager(address=("127.0.0.1", 4444), authkey=b"abc")
print("Client connected")
manager.connect()

if __name__ == '__main__':
    res = manager.get()
    print("result", res)