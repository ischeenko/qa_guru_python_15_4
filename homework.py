
def test_greeting():
    name = "Анна"
    age = 25

    output = f"Привет {name}. Тебе {age} лет."

    assert output == "Привет Анна. Тебе 25 лет."

    print(output)

import math

def test_rectangle():

    a = 10
    b = 20

    perimeter = 2 * (a + b)

    assert perimeter == 60

    area = a * b

    assert area == 200

    print(perimeter)
    print(area)

def test_circle():

   r = 23

   area = (r ** 2) * math.pi

   assert area == 1661.9025137490005

   lenght = 2 * (math.pi * r)

   assert lenght == 144.51326206513048

import random

def test_random_list():
    l = [randint(1, 100) for i in range(10)]

    assert len(l) == 10
    assert all(l[i] <= l[i + 1] for i in range(len(l) - 1))

    print(l)

def test_unique_elemnts():

    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]

    l = list(set(l))

    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(l)


def test_dicts():
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]

    d = dict(zip(first,second))

    assert isinstance(d, dict)
    assert len(d) == 5
    assert list(d.keys()) == first
    assert list(d.values()) == second

    print(d)