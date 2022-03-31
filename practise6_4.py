"""
Реализуйте базовый класс Car
Атрибуты: speed, color, name, is_police (булево)
Методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)

опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""


class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'\nМашина {self.name} {self.color} цвета поехала'

    def stop(self):
        return f'\nМашина {self.name} {self.color} цвета остановилась'

    def turn_direction(self, direction):
        return f'\nМашина {self.name} {self.color} цвета повернула {direction}'

    def show_speed(self):
        return f'\nМашина {self.name} {self.color} цвета двигается со скоростью {self.speed}км/ч'


class Towncar(Car):
    def show_speed(self):
        if self.speed > 60:
            delta = self.speed - 60
            text_1 = f'\nМашина {self.name} {self.color} цвета двигается со скоростью {self.speed}км/ч.'
            text_2 = f'Превышение скорости на {delta} км/ч'
            return f'{text_1} {text_2}'
        else:
            text_1 = f'\nМашина {self.name} {self.color} цвета двигается со скоростью {self.speed}км/ч.'
            text_2 = f'Превышения скорости не наблюдается'
            return f'{text_1} {text_2}'


class Sportcar(Car):
    pass


class Workcar(Car):
    def show_speed(self):
        if self.speed > 40:
            delta = self.speed - 40
            text_1 = f'\nМашина {self.name} {self.color} цвета двигается со скоростью {self.speed}км/ч.'
            text_2 = f'Превышение скорости на {delta} км/ч'
            return f'{text_1} {text_2}'
        else:
            text_1 = f'\nМашина {self.name} {self.color} цвета двигается со скоростью {self.speed}км/ч.'
            text_2 = f'Превышения скорости не наблюдается'
            return f'{text_1} {text_2}'


class Policecar(Car):
    pass


t = Towncar('75', 'red', 'Kia', False)
s = Sportcar('120', 'black', 'BMW', False)
w = Workcar('35', 'white', 'Fiat', False)
p = Policecar('60', 'blue', 'Audi', True)
print(t.go(), t.stop(), t.turn_direction('направо'), t.show_speed())
print(s.go(), s.stop(), s.turn_direction('налево'), s.show_speed())
print(w.go(), w.stop(), w.turn_direction('налево'), w.show_speed())
print(p.go(), p.stop(), p.turn_direction('направо'), p.show_speed())
