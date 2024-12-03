#### Создание датасета

В данном разделе реализованы подходы к созданию датасета в формате Method2Test при обработке Open Sorce датасета [Arain/UnitTest-Finetuning](VK-Technopark-project-2024/data/data_Arain_unitTest-FineTuning_example).

Файлы:

* [create_dataset_m2t_lab.ipynb](VK-Technopark-project-2024/dataset/create_dataset_m2t_lab.ipynb) - творческая и техническая лаборатория обработки датасета.

* [create_dataset_example.ipynb](VK-Technopark-project-2024/dataset/create_dataset_example.ipynb) - файл .ipynb для демонстрации получения датасета.

* [create_dataset_to_input_lab.ipynb](VK-Technopark-project-2024/dataset/create_dataset_to_input_lab.ipynb) - творческая и техническая лаборатория обработки финального датасета.

* [create_dataset_to_input_example.ipynb](VK-Technopark-project-2024/dataset/create_dataset_to_input_example.ipynb) - файл .ipynb для демонстрации получения финального датасета.

* [create_dataset_m2t.py](VK-Technopark-project-2024/dataset/create_dataset_m2t.py) - файл с классом Code2TestPrepareDataset для получения готового обработанного датасета кода. UPD: Добавлен дочерний класс Code2TestPrepareToInput, приводящий датасет к финальному виду перед подачей в сеть.