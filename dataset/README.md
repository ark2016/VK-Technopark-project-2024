#### Создание датасета

В данном разделе реализованы подходы к созданию датасета в формате Method2Test при обработке Open Sorce датасета [Arain/UnitTest-Finetuning](https://huggingface.co/datasets/Arain/UnitTest-Finetuning).

Файлы:

* [create_dataset_m2t_lab.ipynb](create_dataset_m2t_lab.ipynb) - творческая и техническая лаборатория обработки датасета.

* [create_dataset_example.ipynb](create_dataset_example.ipynb) - файл .ipynb для демонстрации получения датасета.

* [create_dataset_to_input_lab.ipynb](create_dataset_to_input_lab.ipynb) - творческая и техническая лаборатория обработки финального датасета.

* [create_dataset_to_input_example.ipynb](create_dataset_to_input_example.ipynb) - файл .ipynb для демонстрации получения финального датасета.

* [create_dataset_m2t.py](create_dataset_m2t.py) - файл с классом Code2TestPrepareDataset для получения готового обработанного датасета кода. UPD: Добавлен дочерний класс Code2TestPrepareToInput, приводящий датасет к финальному виду перед подачей в сеть.
