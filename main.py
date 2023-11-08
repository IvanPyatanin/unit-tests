def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    return b ** 2 - 4 * a * c


def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    if discriminant(a, b, c) < 0:
        return 'корней нет'
    elif discriminant(a, b, c) == 0:
        x = (-b + discriminant(a, b, c) ** 0.5) / (2 * a)
        return x
    else:
        discriminant(a, b, c) > 0
        x_1 = (-b + discriminant(a, b, c) ** 0.5) / (2 * a)
        x_2 = (-b - discriminant(a, b, c) ** 0.5) / (2 * a)
        return x_1, x_2


if __name__ == '__main__':
    solution(1, 8, 15)
    solution(1, -13, 12)
    solution(-4, 28, -49)