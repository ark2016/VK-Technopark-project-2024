#https://huggingface.co/4ervonec19/SimpleTestGenerator/resolve/main/inference_gptbigcode.py
import torch
import torch.nn as nn

from transformers import AutoTokenizer, AutoModelForCausalLM

import logging

logging.getLogger("transformers").setLevel(logging.ERROR)

import warnings

warnings.filterwarnings("ignore")

prompt_string = ("Generate test cases for a given Python function using its source code. The output should be a series "
                 "of assert statements that verify the function's correctness. \n\nExample:\n\nInput:\n\ndef add(a, b):"
                 "\n\treturn a + b\n \n\nOutput:\n\ndef test_add(a, b):\n\n\tassert add(1, 2) == 3\n\tassert add(-1, 1) "
                 "== 0\n\tassert add(0, 0) == 0\n\tassert add(1.5, 2.5) == 4.0\n\nMy Input:\n\n")
max_length = 512
params_inference = {
    'max_new_tokens': 512,
    'do_sample': True,
    'top_k': 100,
    'top_p': 0.85,
}
num_lines = 5

gpt2_name = "bigcode/gpt_bigcode-santacoder"
saved_model_path = '/Users/chervonikov_alexey/Desktop/result_gpt_bigcode_15_epochs/model_val_loss.pth'
device = "cuda" if torch.cuda.is_available() else "cpu"


class LargeCodeModelGPTBigCode(nn.Module):
    '''Класс для большой языковой модели, которая обрабатывает входной код'''

    def __init__(self, gpt2_name=gpt2_name,
                 prompt_string=prompt_string,
                 params_inference=params_inference,
                 max_length=max_length,
                 device=device,
                 saved_model_path=saved_model_path,
                 num_lines=num_lines,
                 flag_hugging_face=False,
                 flag_pretrained=False):

        '''
        Конструктор класса. Необходим для инициализации модели
        Параметры:
        -gpt2_name: link модели на HuggingFace (default: "bigcode/gpt_bigcode-santacoder")
        -prompt_string: дополнительная обертка для лучшего понимания моделью задачи (default: prompt_string)
        -params_inference: параметры инференса (для использования self.gpt2.generate(**inputs,
                                                                        **inference_params))
        -max_length: максимальное число токенов в последовательности (default: 512)
        -device: устройство (default: cuda or cpu)
        -saved_model_path: путь к затюненной модели
        -num_lines: число линий (ввиду "неконечной" генерации модели)
        -flag_hugging_face: флаг для использования HuggingFace (default: False)
        -flag_pretrained: флаг для инициализации модели затюненными весами
        '''
        super(LargeCodeModelGPTBigCode, self).__init__()

        self.new_special_tokens = ['<FUNC_TOKEN>',
                                   '<INFO_TOKEN>',
                                   '<CLS_TOKEN>',
                                   '<AST_TOKEN>',
                                   '<DESCRIPTION_TOKEN>',
                                   '<COMMENTS_TOKEN>']

        self.special_tokens_dict = {
            'additional_special_tokens': self.new_special_tokens
        }

        self.tokenizerGPT = AutoTokenizer.from_pretrained(gpt2_name, padding_side='left')
        self.tokenizerGPT.add_special_tokens({'pad_token': '<PAD>'})
        self.tokenizerGPT.add_special_tokens(self.special_tokens_dict)
        self.gpt2 = AutoModelForCausalLM.from_pretrained(gpt2_name)
        self.gpt2.resize_token_embeddings(len(self.tokenizerGPT))

        self.max_length = max_length
        self.inference_params = params_inference
        self.additional_prompt = prompt_string
        self.pretrained_path = saved_model_path
        self.device = device
        self.num_lines = num_lines

        if flag_pretrained == True and flag_hugging_face == False:
            if self.device == "cuda":
                self.load_state_dict(torch.load(self.pretrained_path))
            else:
                self.load_state_dict(torch.load(self.pretrained_path,
                                                map_location=torch.device('cpu')))

    # forward call
    def forward(self, input_ids, attention_mask,
                response_ids):

        '''
        Forward call method
        Параметры:
        -input_ids: входные токены
        -attention_mask: маска внимания
        -response_ids: метки
        Returns:
        -результат forward call

        '''
        gpt2_outputs = self.gpt2(input_ids=input_ids,
                                 attention_mask=attention_mask,
                                 labels=response_ids)

        return gpt2_outputs

    @staticmethod
    def decode_sequence(tokens_ids, tokenizer):
        '''
        Декодирование последовательности токенов

        Параметры:
        -tokens_ids: последоавтельность токенов
        -tokenizer: токенизатор
        Returns:
        -code_decoded: Декодированная последовательность
        '''

        code_decoded = tokenizer.decode(tokens_ids, skip_special_tokens=True)
        return code_decoded

    @staticmethod
    def remove_before_substring(text, substring="My Output:"):
        '''
        Вспомогательная утилита, чтобы убрать все лишнее

        Параметры:
        -text: строка
        -substring: подстрока (default: "My Output:")
        Returns:
        -text: обновленный текст
        '''

        index = text.find(substring)
        if index != -1:
            # Вернуть часть строки, начиная с подстроки
            return text[index:]
        return text

    @staticmethod
    def extract_text_between_markers(text, start_marker, end_marker):
        '''
        Утилита для работы с входной строкой (получение чистой входной функции)
        Параметры:
        -text: входная строка
        -start_marker: стартовый маркер
        -end_marker: конечный маркер
        Returns:
        -Отфильтрованный текст

        '''

        start_index = text.find(start_marker)
        end_index = text.find(end_marker)
        if start_index == -1 or end_index == -1 or start_index >= end_index:
            return None
        return text[start_index + len(start_marker):end_index].strip()

    def input_inference(self, code_text):
        '''
        Инференс входной строки кода

        Параметры:
        -code_text: строка с кодом
        Returns:
        -dict: {
            'input_function': input_function,
            'generated_output': output_string
        }
        Словарь в формате input_function + generated_output
        '''
        model_input = self.additional_prompt + code_text + "\n\nMy Output:\n\n"

        def encode_text(text, tokenizer=self.tokenizerGPT):
            encoding = tokenizer.encode_plus(
                text,
                add_special_tokens=True,
                max_length=max_length,
                padding='max_length',
                truncation=True,
                return_attention_mask=True,
                return_tensors='pt',
            )
            input_ids_code_text = encoding['input_ids'].flatten()
            attention_mask_code_text = encoding['attention_mask'].flatten()
            return input_ids_code_text, attention_mask_code_text

        input_ids_focal_method, attention_mask_focal_method = encode_text(model_input)

        self.eval()
        with torch.no_grad():
            inputs = {'input_ids': input_ids_focal_method.unsqueeze(0).to(device),
                      'attention_mask': attention_mask_focal_method.unsqueeze(0).to(device)}

            input_function = self.decode_sequence(tokens_ids=inputs['input_ids'][0],
                                                  tokenizer=self.tokenizerGPT)

            input_function = self.extract_text_between_markers(input_function,
                                                               'My Input:',
                                                               'My Output:'),

            output = self.gpt2.generate(**inputs,
                                        **self.inference_params)

            output_string = self.decode_sequence(tokens_ids=output[0],
                                                 tokenizer=self.tokenizerGPT)

            output_string = self.remove_before_substring(output_string) \
                .replace('My Output:', "") \
                .strip()
            output_string = "\n".join(output_string.splitlines()[:self.num_lines])

        return {
            'input_function': input_function,
            'generated_output': output_string
        }


if __name__ == "__main__":
    CodeModel = LargeCodeModelGPTBigCode(gpt2_name, flag_pretrained=True)
