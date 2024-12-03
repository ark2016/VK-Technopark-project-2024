import numpy as np
import pandas as pd
import re
import ast
import flowchart
import json
import time

import os
import random

from tqdm import tqdm
tqdm.pandas()

# JSON_PATH
data_path = '/Users/chervonikov_alexey/Desktop/projects/Technopark_Autumn_2024/NN_course_project/data'
folder_path = 'data_Arain_unitTest-FineTuning_example'
json_path = 'zero_shot_multi_unit_test.json'

input_json_path = os.path.join(data_path, folder_path, json_path)

# CLASS_M2T_DATASET
class Code2TestPrepareDataset:
    '''Датасет типа code2test для решения задачи генерации тестов к коду'''

    def __init__(self, json_input_path):
        '''
        Конструктор датасета. Создает словарь данных (dict)

        Параметры:
        -self
        -json_input: входной файл в формате .json
        '''
        start_time = time.time()
        try:
            with open(json_input_path, 'r') as file:
                data = json.load(file)  # Загружаем JSON данные
                self.code2test_dict = data  # Объявляем словарь code2test_dict
        except FileNotFoundError:
            print(f"Ошибка: файл {json_input_path} не найден.")
        except json.JSONDecodeError:
            print(f"Ошибка: файл {json_input_path} не является корректным JSON.")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")
        self.code_dataset = pd.DataFrame()  # Пустой code_dataset
        code_dataset = pd.DataFrame(self.code2test_dict)  # создаем code_dataset из словаря json_dict
        code_dataset['query'] = code_dataset['conversations'].map(lambda x: x[0]['value'])  # извлекаем prompt
        code_dataset['response'] = code_dataset['conversations'].map(lambda x: x[1]['value'])  # извлекаем response
        code_dataset = code_dataset.drop(columns=['conversations'])  # убираем conversations

        self.code_dataset = code_dataset  # Объявляем датафрейм
        end_time = time.time()
        print(f"Время инициализации датасета: {end_time - start_time:.3f} секунды")

    def get_dataset(self):
        '''Простой возврат датасета'''
        return self.code_dataset

    @staticmethod
    def check_template_match(input_text: str, get_features: bool = False):
        '''
        Функция проверяет соответствие запроса шаблону

        Параметры:
        - input_text: входной запрос
        - get_features: флаг для осуществления извлечения признаков (default: False)

        Возвращает:
        True если соответствует, иначе False;
        Извлеченные признаки
        '''
        # Регулярное выражение для проверки соответствия шаблону
        pattern = re.compile(
            r"You are a professional (?P<language>\w+) software engineer\. You are asked to generate a complete test class for a focal method in a focal class\.\n"
            r"You will be given the following information of the focal method:"
            r"\n1\. Source code of the focal method\."
            r"\n2\. Source code of the focal class\(Code that is not relevant to focal method's execution is filtered\)\."
            r"\n3\. Source code of callee examples of the focal method\."
            r"\nYou will ONLY return unit test code for the focal method including necessary imports and dependencies, make sure it compile without errors, and use reflection to invoke private methods\. "
            r"\nNote that no additional explanations required\."
            r"\n\nHere are the information of the focal method:"
            r"\n1\. Source code of the focal method\.\n"
            r"(?P<methodCode>.*?)\n"
            r"2\. Source code of the focal class\(Codes that are may not related to focal method are filtered\).\n"
            r"(?P<methodTotalCode>.*?)\n"
            r"3\. Source code of callee examples of the focal method.\n"
            r"(?P<callCode_callees_string>.*?)\n"
            r"\nPlease note that the test class you return should include multiple test cases covering different functionalities. There is no upper limit on the number of test cases, but you need to ensure that the test cases provide high test coverage and test extreme and special cases of the code as much as possible\.\n"
            ,
            re.DOTALL
        )

        # Проверяем соответствие шаблону
        if not get_features:
            return bool(pattern.match(input_text))
        else:
            match = pattern.match(input_text)
            if match:
                return True, (match.group('language'),
                            match.group('methodCode'),
                            match.group('methodTotalCode'),
                            match.group('callCode_callees_string'))
            else:

                return False, None

    @staticmethod
    def process_all_samples_quieries(self):
        '''
        Функция для проверки запросов всех сэмплов на соответствие шаблону, указанному на HuggingFace

        Параметры:
        -dataset: датасет с кодом (default: code_dataset)
        '''
        for i in tqdm(range(self.code_dataset.shape[0])):  # Проходимся и проверяем на True
            assert (Code2TestPrepareDataset.check_template_match(
                self.code_dataset.iloc[i, 1]) == True), "CODE DOESN'T MATCH THE TEMPLATE"

    @staticmethod
    def query_processing_map(query):
        '''Вспомогательная функция для реализации pandas.map'''
        _, features = Code2TestPrepareDataset.check_template_match(query, get_features=True)
        return features

    @staticmethod
    def get_comments_and_description(text_code: str):
        '''
        Функция извлекает все комментарии из кода и описания функций:

        Параметры:
        -text_code: строка с кодом

        '''

        # Шаблоны для поиска комментариев и описаний
        triple_quotes_pattern = r'"""(.*?)"""|\'\'\'(.*?)\'\'\''
        single_comment_pattern = r'#.*'

        # Извлекаем
        triple_quotes_matches = re.findall(triple_quotes_pattern, text_code, re.DOTALL)
        single_comment_matches = re.findall(single_comment_pattern, text_code)

        docstrings = [match[0] or match[1] for match in triple_quotes_matches]
        comments = single_comment_matches

        return ("\n".join(docstrings), "\n".join(comments))

    @staticmethod
    def clean_text_code(text_code: str) -> str:
        '''
        Фунция для чистки кода от .md команд

        Параметры:
        -text_code: код в формате строки

        Возвращает "чистый" код

        '''
        cleaned_code = re.sub(r"^```python\n|^```\n|```$", "", text_code, flags=re.MULTILINE)
        return cleaned_code

    @staticmethod
    def get_ast_representation(text_code: str) -> str:
        """
        Получает AST-дерево для кода. Если возникает ошибка при парсинге, возвращает строку 'AST_TOKEN'.

        Параметры:
        - text_code: код в виде текста

        Возвращает AST-дерево или 'AST_TOKEN' в случае ошибки.
        """
        try:
            # Пытаемся сразу построить AST-дерево
            tree = ast.parse(text_code)
            # Преобразуем AST в строку и возвращаем
            ast_tree = ast.dump(tree, indent=4)
            return ast_tree
        except SyntaxError:
            # Если ошибка, возвращаем 'AST_TOKEN'
            return "AST_TOKEN"

    def prepare_dataset(self):
        '''Функция подготовки датасета'''

        start_time_ = time.time()

        start_time = time.time()
        self.process_all_samples_quieries(self)  # Проверка на соответствие представленному шаблону
        end_time = time.time()
        print(f"Время проверки формата запросов: {end_time - start_time:.3f} секунды")

        # Извлекаем признаки из текста
        start_time = time.time()
        self.code_dataset['code_features'] = self.code_dataset['query'].progress_apply(
            lambda query: self.query_processing_map(query))
        self.code_dataset['LANG_TOKEN'] = self.code_dataset['code_features'].progress_apply(
            lambda features: features[0])
        self.code_dataset['focal_method'] = self.code_dataset['code_features'].progress_apply(
            lambda features: features[1])
        self.code_dataset['focal_cls'] = self.code_dataset['code_features'].progress_apply(lambda features: features[2])
        self.code_dataset['callee'] = self.code_dataset['code_features'].progress_apply(lambda features: features[3])
        end_time = time.time()
        print(f"Время извлечения глобальных признаков из текста кода: {end_time - start_time:.3f} секунды")

        # Извлекаем описание и комментарии

        # Для focal_method
        start_time = time.time()
        self.code_dataset['focal_method_docs'] = self.code_dataset['focal_method'].progress_apply(
            lambda x: self.get_comments_and_description(x)[0])
        self.code_dataset['focal_method_comments'] = self.code_dataset['focal_method'].progress_apply(
            lambda x: self.get_comments_and_description(x)[1])

        # Для focal_cls
        self.code_dataset['focal_cls_docs'] = self.code_dataset['focal_cls'].progress_apply(
            lambda x: self.get_comments_and_description(x)[0])
        self.code_dataset['focal_cls_comments'] = self.code_dataset['focal_cls'].progress_apply(
            lambda x: self.get_comments_and_description(x)[1])

        # Для calle
        self.code_dataset['callee_docs'] = self.code_dataset['callee'].progress_apply(
            lambda x: self.get_comments_and_description(x)[0])
        self.code_dataset['callee_comments'] = self.code_dataset['callee'].progress_apply(
            lambda x: self.get_comments_and_description(x)[1])
        end_time = time.time()
        print(f"Время извлечения комментариев и описаний из текста кода: {end_time - start_time:.3f} секунды")

        # "Чистый" код
        start_time = time.time()
        self.code_dataset['focal_method'] = self.code_dataset['focal_method'].progress_apply(
            lambda x: self.clean_text_code(x))
        self.code_dataset['focal_cls'] = self.code_dataset['focal_cls'].progress_apply(
            lambda x: self.clean_text_code(x))
        self.code_dataset['callee'] = self.code_dataset['callee'].progress_apply(lambda x: self.clean_text_code(x))
        self.code_dataset['response'] = self.code_dataset['response'].progress_apply(lambda x: self.clean_text_code(x))
        end_time = time.time()
        print(f"Время очистки текста кода: {end_time - start_time:.3f} секунды")

        # ast-парсинг
        start_time = time.time()
        self.code_dataset['focal_method_ast'] = self.code_dataset['focal_method'].progress_apply(
            lambda x: self.get_ast_representation(x))
        self.code_dataset['focal_cls_ast'] = self.code_dataset['focal_cls'].progress_apply(
            lambda x: self.get_ast_representation(x))
        self.code_dataset['callee_ast'] = self.code_dataset['callee'].progress_apply(
            lambda x: self.get_ast_representation(x))
        end_time = time.time()
        print(f"Время получения ast-деревьев на основе текста кода: {end_time - start_time:.3f} секунды")

        end_time_ = time.time()
        print(f"Время подготовки датасета: {end_time_ - start_time_:.3f} секунды")

class Code2TestPrepareToInput(Code2TestPrepareDataset):
    '''
    Дочерний класс для финальной подготовки датасета 
    '''
    def __init__(self, json_input_path):
        '''Конструктор из родительского класса'''
        super().__init__(json_input_path)

    @staticmethod
    def remove_docs(row, col_name, docs_col_name):
        '''Функция удаления описания из указанной колонки'''
        return row[col_name].replace(row[docs_col_name], '')

    @staticmethod
    def remove_three_quotes(row, col_name):
        '''Функция удаления """""" из указанной колонки'''
        return row[col_name].replace('""""""', '')
    
    @staticmethod
    def remove_three_quotes_v2(row, col_name):
        '''Функция удаления '''''' из указанной колонки'''
        return row[col_name].replace('''''''', '')
    
    @staticmethod
    def drop_ln(row, col_name):
        '''Функция удаления \n из указанной колонки'''
        return row[col_name].replace('\n', '')

    @staticmethod
    def drop_large_spaces(row, col_name):
        '''Функция удаления длинных пробелов (\t) из указанной колонки'''
        cleaned_string = re.sub(r'\s+', ' ', row[col_name])
        return cleaned_string

    @staticmethod
    def remove_comment(row, col_name, comments_col_name):
        '''Функция удаления комментариев из указанной колонки'''
        return row[col_name].replace(row[comments_col_name], '')
    
    @staticmethod
    def drop_hashtag_symbol(row, col_name):
        '''Функция отбрасывает символ # для указанной колонки'''
        return row[col_name].replace('#', '')

    @staticmethod
    def remove_non_language_symbols(row, col_name):
        '''Функция удаления неалфавитных символов из указанной колонки'''
        return re.sub(r'[^a-zA-Z0-9\s]', '', row[col_name])

    @staticmethod
    def strip_text(row, col_name):
        '''Функция удаления пробелов в начале и в конце строки для указанной колонки'''
        return row[col_name].strip()
    
    @staticmethod
    def create_NL_code_representation(row, desc_col, comm_col):
        '''Функция создания описания'''
        result = "DESCRIPTION_TOKEN: {} COMMENTS_TOKEN: {}".format(row[desc_col], row[comm_col])
        return result

    @staticmethod
    def replace_empty_info(row, info_col):
        '''Функция для определения пустого описания'''
        return row[info_col].replace("DESCRIPTION_TOKEN:  COMMENTS_TOKEN: ", "INFO_TOKEN")

    @staticmethod
    def replace_INFO_TOKEN_non_empty(row, info_col):
        '''Функция замены INFO_TOKEN при условии не равенства строки INFO_TOKEN'''
        if row[info_col] == 'INFO_TOKEN':
            return 'INFO_TOKEN'
        return row[info_col].replace('INFO_TOKEN', 'DESCRIPTION_TOKEN: ')
    
    @staticmethod
    def remove_triple_quotes_content(row, col_name):
        '''Функция для удаления содержимого внутри тройных кавычек'''
        # Регулярное выражение для поиска содержимого внутри тройных кавычек
        pattern = re.compile(r'""".*?"""', re.DOTALL)
        # Замена содержимого внутри тройных кавычек на пустую строку
        return pattern.sub('', row[col_name])
    
    @staticmethod
    def replace_func(row, column_fm, column_fc):
        '''Функция будет заменять содержимое одной колонки внутри другой'''
        target = row[column_fc]
        substring = row[column_fm]
        return target.replace(substring, 'FUNC_TOKEN')

    @staticmethod
    def insert_space(row, column, token):
        '''Функция вставить пробел дополнительный пробел для токена в колонке'''
        return row[column].replace(token, f" {token} ").strip().replace('  ', ' ')

    def prepare_dataset(self):
        '''Расширение функциональности родительского prepare_dataset()'''
        super().prepare_dataset()

        start = time.time()
        self.code_dataset = self.code_dataset.drop(columns=['callee', 
                                                            'callee_docs', 
                                                            'callee_comments', 
                                                            'callee_ast']) # Выбрасывем callee колонки

        # Готовим focal_method
        start_time = time.time()
        self.code_dataset['focal_method'] = self.code_dataset.progress_apply(self.remove_docs, axis=1, args=('focal_method', 'focal_method_docs'))
        self.code_dataset['focal_method'] = self.code_dataset.progress_apply(self.remove_three_quotes, axis=1, args=('focal_method',))
        self.code_dataset['focal_method'] = self.code_dataset.progress_apply(self.remove_three_quotes_v2, axis=1, args=('focal_method',))
        self.code_dataset['focal_method'] = self.code_dataset.progress_apply(self.drop_ln, axis=1, args=('focal_method',))
        self.code_dataset['focal_method'] = self.code_dataset.progress_apply(self.drop_large_spaces, axis=1, args=('focal_method',))
        self.code_dataset['focal_method'] = self.code_dataset.progress_apply(self.remove_comment, axis=1, args=('focal_method', 'focal_method_comments'))

        self.code_dataset['focal_method_comments'] = self.code_dataset.progress_apply(self.drop_hashtag_symbol, axis=1, args=('focal_method_comments',))
        self.code_dataset['focal_method_comments'] = self.code_dataset.progress_apply(self.drop_ln, axis=1, args=('focal_method_comments',))
        self.code_dataset['focal_method_comments'] = self.code_dataset.progress_apply(self.drop_large_spaces, axis=1, args=('focal_method_comments',))
        self.code_dataset['focal_method_comments'] = self.code_dataset.progress_apply(self.remove_non_language_symbols, axis=1, args=('focal_method_comments',))
        self.code_dataset['focal_method_comments'] = self.code_dataset.progress_apply(self.strip_text, axis=1, args=('focal_method_comments',))
        
        self.code_dataset['focal_method_info'] = self.code_dataset.progress_apply(
            self.create_NL_code_representation, axis=1, args=('focal_method_docs', 'focal_method_comments')
        )
        self.code_dataset['focal_method_info'] = self.code_dataset.progress_apply(
            self.replace_empty_info, axis=1, args=('focal_method_info',)
        )
        self.code_dataset['focal_method_info'] = self.code_dataset.progress_apply(
            self.replace_INFO_TOKEN_non_empty, axis=1, args=('focal_method_info',)
        )
        self.code_dataset = self.code_dataset[self.code_dataset['focal_method_ast'] != 'AST_TOKEN']
        self.code_dataset['focal_method_info'] = self.code_dataset.progress_apply(self.drop_ln, axis=1, args=('focal_method_info',))
        self.code_dataset['focal_method_info'] = self.code_dataset.progress_apply(self.drop_large_spaces, axis=1, args=('focal_method_info',))
        self.code_dataset['focal_method_ast'] = self.code_dataset.progress_apply(self.drop_ln, axis = 1, args = ['focal_method_ast'])
        self.code_dataset['focal_method_ast'] = self.code_dataset.progress_apply(self.drop_large_spaces, axis = 1, args = ['focal_method_ast'])
        self.code_dataset = self.code_dataset.drop(columns=['focal_method_docs', 
                                'focal_method_comments'])
        
        # Готовим focal_cls
        end_time = time.time()
        print(f"Время подготовки focal_method: {end_time - start_time:.3f} секунды")
        
        start_time = time.time()
        self.code_dataset['focal_cls'] = self.code_dataset.progress_apply(self.remove_triple_quotes_content, axis = 1, args = ['focal_cls'])
        self.code_dataset['focal_cls'] = self.code_dataset.progress_apply(self.remove_docs, axis=1, args=('focal_cls', 'focal_cls_docs'))
        self.code_dataset['focal_cls'] = self.code_dataset.progress_apply(self.remove_three_quotes, axis=1, args=('focal_cls',))
        self.code_dataset['focal_cls'] = self.code_dataset.progress_apply(self.remove_three_quotes_v2, axis=1, args=('focal_cls',))
        self.code_dataset['focal_cls'] = self.code_dataset.progress_apply(self.drop_ln, axis=1, args=('focal_cls',))
        self.code_dataset['focal_cls'] = self.code_dataset.progress_apply(self.drop_large_spaces, axis=1, args=('focal_cls',))
        self.code_dataset['focal_cls'] = self.code_dataset.progress_apply(self.remove_comment, axis=1, args=('focal_cls', 'focal_cls_comments'))
        self.code_dataset['focal_cls'] = self.code_dataset.progress_apply(self.replace_func, axis=1, args=('focal_method', 'focal_cls'))
        self.code_dataset['focal_cls'] = self.code_dataset.progress_apply(self.insert_space, axis=1, args=('focal_cls', 'FUNC_TOKEN'))
        self.code_dataset['focal_cls_info'] = self.code_dataset.progress_apply(
            self.create_NL_code_representation, axis=1, args=('focal_cls_docs', 'focal_cls_comments')
        )
        self.code_dataset['focal_cls_info'] = self.code_dataset.progress_apply(
            self.replace_empty_info, axis=1, args=('focal_cls_info',)
        )
        self.code_dataset['focal_cls_info'] = self.code_dataset.progress_apply(
            self.replace_INFO_TOKEN_non_empty, axis=1, args=('focal_cls_info',)
        )
        self.code_dataset['focal_cls_info'] = self.code_dataset.progress_apply(self.drop_ln, axis=1, args=('focal_cls_info',))
        self.code_dataset['focal_cls_info'] = self.code_dataset.progress_apply(self.drop_large_spaces, axis=1, args=('focal_cls_info',))
        self.code_dataset = self.code_dataset.drop(columns=['focal_cls_docs', 
                                'focal_cls_comments'])
        
        self.code_dataset['focal_cls_ast'] = self.code_dataset.progress_apply(self.drop_ln, axis = 1, args = ['focal_cls_ast'])
        self.code_dataset['focal_cls_ast'] = self.code_dataset.progress_apply(self.drop_large_spaces, axis = 1, args = ['focal_cls_ast'])
        
        end_time = time.time()
        print(f"Время подготовки focal_cls: {end_time - start_time:.3f} секунды")
        end = time.time()
        print(f"Время подготовки датасета: {end - start:.3f} секунды")

# MAIN
def main():
    m2t_dataset = Code2TestPrepareDataset(input_json_path)
    m2t_dataset.prepare_dataset()
    return m2t_dataset.get_dataset()

if __name__ == '__main__':
    main()
