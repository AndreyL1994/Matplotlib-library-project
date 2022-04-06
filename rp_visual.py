import matplotlib.pyplot as plt

from random_points import RandomPoints

while True:
    # Построение случайных точек.
    rp = RandomPoints()
    rp.calculation_points()

    # Нанесение точек на диаграмму.
    plt.style.use('dark_background')    # Выбираем стиль графика
    fig, ax = plt.subplots(figsize=(15, 9))    # Задаем размер окошка с графиком
    points = range(rp.points)
    ax.scatter(rp.x_values, rp.y_values, c=points, cmap=plt.cm.Blues,    # Задаем параметры графика разброса точек
               edgecolors='none', s=5)

    # Выделение первой и последней точек.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rp.x_values[-1], rp.y_values[-1], c='red', edgecolor='none',
               s=100)

    # Удаляем оси графика
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    another_walk = input("Make another walk? (y/n): ")
    if another_walk == 'n':
        break
