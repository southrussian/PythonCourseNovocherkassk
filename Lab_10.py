# Написать функцию, которая генерирует шесть случайных чисел между 30 и 100
import random


def generate_random_numbers():
    lst = []
    for i in range(6):
        lst.append(random.randint(30, 100))
    return lst


let = generate_random_numbers()
print(let)
