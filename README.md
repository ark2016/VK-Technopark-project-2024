# Data Mining и Построение метрик

Сам датасет (не разделённый на train и test) лежит в файле `data_mining/functions_tests.csv`  
В данный момент в нем 200 семплов.

---

Все, что дальше - справочная информация, если есть желание "потыкать, что тут ещё есть"  

---  

Тесты находятся в папке `data_mining/`  

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