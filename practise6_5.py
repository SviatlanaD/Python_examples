"""
Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка)
Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw.
Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки с помощью {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки с помощью {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки с помощью {self.title}'


p = Pen('Шириковая ручка')
pl = Pencil('Графитофый карандаш ТМ')
h = Handle('Перманентный маркер')
print(p.draw())
print(pl.draw())
print(h.draw())
