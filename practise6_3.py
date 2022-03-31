"""
Реализовать базовый класс Worker (работник)
определить атрибуты:
    name, surname, position (должность),
    income (доход) - последний атрибут должен быть защищённым и ссылаться на словарь,
        содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения:
    полного имени сотрудника (get_full_name)
    дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных:
    создать экземпляры класса Position
    передать данные
    проверить значения атрибутов
    вызвать методы экземпляров.
"""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        fio = self.surname + ' ' + self.name
        print(f'ФИО сотрудника {fio}')

    def get_total_income(self):
        fio = self.surname + ' ' + self.name
        b = self._income["wage"] + self._income["bonus"]
        print(f'Доход с учетом премии {fio} составляет {b}')


p = Position('Иван', 'Иванов', 'инженер', '200', '10')
p.get_full_name()
p.get_total_income()
