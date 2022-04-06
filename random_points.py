from random import choice


class RandomPoints():
    """Класс генерирует случайную расстоновку точек."""

    def __init__(self, points=10000):
        """Инициализирует атрибуты расстовновки точек."""
        self.points = points

        # Движение начинается с точки (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def calculation_points(self):
        """Вычисляет все точки"""

        while len(self.x_values) < self.points:
            # Генерирование шагов.
            x_route = choice([1, -1])    # определяет направление движения
            x_distance = choice([0, 1, 2, 3, 4])   # Определяет дистанцию перемещения
            x_step = x_route * x_distance    # Определяет шаг

            y_route = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_route * y_distance

            # Отклонение нулевых перемещений.
            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
