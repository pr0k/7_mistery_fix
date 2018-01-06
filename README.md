# Решатель квадратных уравнений

* **quadratic_equation.py** содержит метод расчета корней квадратного уравнения.  
* **tests.py** реализует блок проверок на допустимость полученных значений корней, в зависимости от введеных аргументов.

# Как использовать

## Нахождение корней квадратного уравнения

**quadratic_equation.py** использует следующие модули:
```python
# quadratic_equation.py

import math
```

Непосредственный расчёт дискриминанта и нахождение корней происходит внутри функции 
`get_roots()`, в которую передаются целочисленные значения, являющиеся аргументами квадратного уравнения:
```python
get_roots(a, b, c)
```

При необходимости можно использовать метод `get_roots()` в любом внешнем модуле:
```python
# some_name.py

from quadratic_equation import get_roots
```

## Тестирование результирующих значений 
Полученные корни квадратного уравнения подвергаются проверке на допустимость, при текущих значениях аргументов функции `get_roots()`, внутри тестового модуля **tests.py**.  
**tests.py** реализован на основе встроенного модуля **unittest**, который поддерживает автоматизацию тестов.  
Для запуска проверки нужно подключить следующие модули:
```python
import unittest
from quadratic_equation import get_roots
```

Результатом выполнения будет отчет по аналогии с этим:
```python
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