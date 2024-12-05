# Data Mining и Построение метрик

### Данные для обучения лежат в папке `data`.  
Данные помечены по версиям, необходимо считать, что имеющая наибольший порядковый номер -- рабочая.  

[01_functions_tests_200.csv](data%2F01_functions_tests_200.csv) - Первый вариант, содержит 200 функций  
[02_functions_tests_600.csv](data%2F02_functions_tests_600.csv) - Добавлены ещё 400 функций, код тестов больше соответствует стандартам

В папке `data/data_with_metric` лежат те же датасеты, только с подсчитанными значениями метрик  

---

### Модуль оценки метрик  
находится в директории `metric_module`  
Для использования напрямую из него можно импортировать 2 функции:  `coverage_percent` и `calculate_coverage_for_df`
Примеры использования этого модуля представлены в файле [metric_example.py](metric_example.py)  

### Для того, чтобы модуль корректно работал необходимо несколько условий:  
1. Перед началом функции кода или тестов не должно быть символов
2. В коде или тестах не должно быть импортов
3. Каждая строчка внутри функции тестов -- это отдельный assert (не должно быть такого, чтобы один тест был разделён на несколько строк)

### Принцип работы модуля следующий:

- Вначале функция теста разбивается на несколько независимых тестирующих функций  
Было:
```python
def test_is_even():
    assert is_even(4) is True
    assert is_even(0) is True
    assert is_even(2) is True
    assert is_even(3) is False
```
- Стало:  
```python
def test_is_even_1():
    assert is_even(4) is True

def test_is_even_2():
    assert is_even(0) is True

def test_is_even_3():
    assert is_even(2) is True

def test_is_even_4():
    assert is_even(3) is False
```
- После этого запускается отдельный процесс для тестирования кода.
- К коду теста добавляется подключение файла функции и библиотека `pytest`.
- Во время выполнения тестирования код функции и код тестов сохраняются в 2 временных файла.
- Производится выполнение этих файлов и подсчет статистики.

Функция `coverage_percent` принимает функцию и тестовую функцию в виде строк и возвращает 3 значения: процент покрытия, количество ошибок выполнения, список пропущенных строк.

Функция `calculate_coverage_for_df` принимает датафрейм (в том формате, в котором сделаны данные для обучения в папке data) и
возвращает другой датафрейм (исходный датафрейм не изменяется), который помимо исходных столбцов содержит столбцы coverage_percent (процент покрытия) и Errors
(количество ошибок).

---

Все, что дальше - справочная информация, если есть желание "потыкать, что тут ещё есть".  

---  

Всё, что связано с генерацией и проверкой тестов находится в папке `data_mining/`.  

Все 1200 тестируемых функций находятся в `data_mining/functions.py`.  
Все, написанные на данный момент тестовые функции находятся в `data_mining/tests.py`.

Функции `split_func.py`, `create_df.py` и `reformat.py` в `data_mining/` предназначены для форматирования и разбиения файлов с функциями и тестами.  

В папке `data_mining/tests/functions` лежат функции из `functions.py` разбитые по 20 штук.  
В `data_mining/tests/` лежат тесты разбитые по 20 штук.  

Для того чтобы проверить покрытие функций написанными тестами, нужно выполнить следующее:  
  
Установить библиотеки для тестирования кода:  
```bash
pip install -r requirements.txt
```
  
Перейти в папку с тестами:  
```bash
 cd data_mining/tests
  ```  

  
Запустить проверку покрытия во всех совместимых файлах в директории:  
```bash
 coverage run -m pytest .
  ```
  
Проверить покрытие:  
```bash
 coverage report -m
  ```
  
Если нужно посмотреть подробности, то выполнить:  
```bash
 coverage html
  ```
  
Это создаст в директории `data_mining/tests/` папку `htmlcov` в ней нужно найти файл `index.html` и открыть его в браузере.