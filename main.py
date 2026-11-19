import numpy as np

# Задание 1

numbers = [4, 8, 2, 15, 6]
arr = np.array(numbers)

print(type(arr))
print(arr.shape)
print(arr.size)
print(arr)

# Задание 2

celsius = np.array([0, 10, 20, 30, 40])
fahrenheit = celsius * 9 / 5 + 32

print("Цельсии:   ", celsius)
print("Фаренгейты:", fahrenheit)

# Задание 3

times = np.array([115, 92, 84, 108, 73, 121, 89])

print("Среднее время:     ", np.mean(times))
print("Максимум:          ", np.max(times))
print("Минимум:           ", np.min(times))
print("Станд. отклонение: ", np.std(times))
print("Сумма:             ", np.sum(times))

# Задание 4

weights = np.array([[0.1, 0.2, 0.3],
                    [0.4, 0.5, 0.6],
                    [0.7, 0.8, 0.9]])

print("Матрица:\n", weights)
print("Форма матрицы:     ", weights.shape)
print("Первая строка:     ", weights[0, :])
print("Последний столбец: ", weights[:, -1])
print("Элемент [1][2]:    ", weights[1, 2])

# Задание 5

randoms = np.random.randint(1, 101, size=100)

mask = randoms > 50
big = randoms[mask]

print("Всего чисел:      ", randoms.size)
print("Чисел больше 50:  ", big.size)
print("Отобранные числа: ", big)

# Задание 6

grades = np.array([[5, 4, 3],
                   [4, 4, 5],
                   [3, 5, 5],
                   [4, 3, 4],
                   [5, 5, 4]])

by_student = grades.mean(axis=1)
by_subject = grades.mean(axis=0)

print("Средний балл каждого студента:", by_student)
print("Средний балл по предметам:    ", by_subject)