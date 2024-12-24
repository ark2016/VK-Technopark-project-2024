#### Learning & Inference

В данном разделе реализуется обучение и инстанцируется класс для загрузки весов обученной модели (fine-tuning) с дальнейшим проведение инференса.

#### HuggingFace Model

Обученная модель была загружена на [HuggngFace](https://huggingface.co/4ervonec19/SimpleTestGenerator). Поэтому открыта возможность для использования API для инференса модели.

#### Файлы

* [logs_tensorboard](logs_tensorboard) - папка с логами TensorBoard, полученными во время обучения.

* [logs_gptbigcode.txt](logs_gptbigcode.txt) - .txt файл с output, полученными при обучении модели.

* [input_code_dataset_inference_upd.csv](input_code_dataset_inference_upd.csv) - входной датасет типа input-output.

* [output_code_tests_dataset.csv](output_code_tests_dataset.csv) - выходной датасет для валидационного подмножества.

* [language_models_train_decoder_inference_15_epochs.ipynb](language_models_train_decoder_inference_15_epochs.ipynb) - .ipynb файл с препроцессингом и обучением модели.

* [inference_gptbigcode.py](inference_gptbigcode.py) - .py файл с классом модели, содержащей конструктор и методы, необходимые для инференса.

* [inference_example.ipynb](inference_example.ipynb) - .ipynb с примером инференса модели.

* [HuggingFace_inference_example.ipynb](HuggingFace_inference_example.ipynb) - .ipynb с примером инференса по ссылке с [HuggngFace](https://huggingface.co)