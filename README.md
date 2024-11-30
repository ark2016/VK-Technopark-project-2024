# Построение метрик

Тесты находятся в папке data_mining  
Все 1200 тестируемых функций находятся в `data_mining/functions.py`
Все, написанные на данный момент тестовые функции находятся в `data_mining/tests.py`

Функции `split_func.py` и `reformat.py` в `data_mining/` предназначены для форматирования и разбиения файлов с функциями и тестами  

В папке `data_mining/tests/functions` лежат функции из `functions.py` разбитые по 20 штук.  
В `data_mining/tests/` лежат тесты разбитые по 20 штук.  

Для того чтобы проверить покрытие функций написанными тестами, нужно выполнить следующее:  
Перейти в папку с тестами:  
```cd data_mining/tests```  
  
Запустить проверку покрытия во всех совместимых файлах в директории:  
```coverage run -m pytest .```
  
Проверить покрытие:  
```coverage report -m```
  
Если нужно посмотреть подробности, то выполнить:  
```coverage html```
  
Это создаст в директории `data_mining/tests/` папку `htmlcov` в ней нужно найти файл `index.html` и открыть его в браузере.