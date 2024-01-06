from queue import Queue, SimpleQueue


class FirstFifo(object):
    """Класс для реализации очереди типа FIFO (first in, first out) в ручном виде (без циклов заполнения и удаления).

    При создании экземпляра класса, в необязательном порядке указывается размер очереди.
    Создается два указателя: current_to_append - индекс для добавления элемента, first_to_delete - индекс для удаления
    элемента. Так же сама очередь data - список нулей.

    Вся суть в перестановке указателей и работе с отрицательными индексами (для избежания ошибок в условиях).
    Для удобства переопределен метод __str__ на вывод всей очереди.
    """

    def __init__(self, size: int = 7) -> None:
        self.size = size
        self.current_to_append = -self.size
        self.first_to_delete = 0
        self.data = [0 for _ in range(self.size)]

    def append(self, value: all) -> None:
        if self.current_to_append == self.size:
            self.current_to_append = 0
        if self.current_to_append == self.first_to_delete:
            print('Очередь полная!')
        else:
            self.data[self.current_to_append] = value
            self.current_to_append += 1

    def pop(self) -> None:
        if self.first_to_delete == self.size:
            self.first_to_delete = -self.size
            self.data[self.first_to_delete] = 0
            self.first_to_delete += 1
        else:
            self.data[self.first_to_delete] = 0
            self.first_to_delete += 1

    def __str__(self) -> str:
        return str(self.data)


class SecondFifo(Queue):

    def __iter__(self):
        return self

    def __next__(self):
        if not self.empty():
            return self.get()
        else:
            raise StopIteration

    def __str__(self) -> str:
        output = str(self.queue)[str(self.queue).find('(') + 1:str(self.queue).find(')')]
        # output = [self.get() for _ in range(self.qsize())]
        return str(output)
