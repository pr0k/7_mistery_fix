# Решатель квадратных уравнений

[Данный скрипт демонстрирует расчет корней квадратного уравнения и проверку на допустимость значений корней в зависимости от введеных аргументов]

# Как использовать

Для работы скрипта используются следующие модули:
```bash
# tests.py

import unittest
from quadratic_equation import get_roots
```

В get_roots передаются целочисленные значения, которые являются аргументами квадратного уравнения:
```bash
get_roots(a, b, c)
```

Полученные корни квадратного уравнения подвергаются проверке на допустимость при текущих значениях аргументов функции get_roots:
```bash
    def test_solves_real_roots(self):
        root1, root2 = get_roots(1, -2, 1)
        self.assertEqual(root1, 1)

    def test_first_root_less_than_second(self):
        root1, root2 = get_roots(1, 2, -3)
        self.assertEqual(root1, -3)
        self.assertEqual(root2, 1)

    def test_second_root_is_none_if_one_solution(self):
        root1, root2 = get_roots(1, -2, 1)
        self.assertIsNotNone(root1)
        self.assertIsNone(root2)

    def test_returns_none_for_complex_solution(self):
        root1, root2 = get_roots(1, 2, 3)
        self.assertIsNone(root1)
        self.assertIsNone(root2)
```

Результатом выполнения будет отчет по аналогии с этим:
```bash
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```


# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash
python tests.py # может понадобиться вызов python3 вместо python, зависит от настроек операционной системы
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
