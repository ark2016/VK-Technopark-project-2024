# Файл с инструментами, необходимыми для обучения
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader, random_split
from transformers import AutoTokenizer, AutoModel, AutoConfig, GPT2LMHeadModel
from transformers import GPT2LMHeadModel


# Новые служебные токены
new_special_tokens = ['<FUNC_TOKEN>',
            '<INFO_TOKEN>',
            '<CLS_TOKEN>', 
            '<AST_TOKEN>', 
            '<DESCRIPTION_TOKEN>',
            '<COMMENTS_TOKEN>']


# Токенизатор
tokenizer_code_bert = AutoTokenizer.from_pretrained("microsoft/codebert-base", output_hidden_states= True)

# Слоаврь дополнительных токенов
special_tokens_dict = {
    'additional_special_tokens': new_special_tokens
}

# Добавляем токены
tokenizer_code_bert.add_special_tokens(special_tokens_dict)

tokenizerGPT = AutoTokenizer.from_pretrained("gpt2")
tokenizerGPT.add_special_tokens({'pad_token': '<PAD>'})

modelGPT2Path = "gpt2"
config = AutoConfig.from_pretrained(modelGPT2Path, is_decoder=True, add_cross_attention= True)
config.add_cross_attention = True  # Включение cross-attention

modelGPT2 = AutoModel.from_pretrained(modelGPT2Path, config=config)
modelGPT2.resize_token_embeddings(len(tokenizerGPT))

def tokenization_example(input_str: str):
	'''Функция отображения результатов токенизации'''
	code_bert_tokens_example = tokenizer_code_bert.tokenize(input_str)
	code_bert_tokens_ids = tokenizer_code_bert.convert_tokens_to_ids(code_bert_tokens_example)
	code_bert_decoded = tokenizer_code_bert.decode(code_bert_tokens_ids)
	print(f"Длина закодированной последовательности: {len(code_bert_tokens_example)}")
	print(f"Как выглядят токены исходной фразы: {code_bert_tokens_example}")
	print(f"Индексы токенов: {code_bert_tokens_ids}")
	print(f"Декодированная строка: {code_bert_decoded}")
	
def decode_sequence(tokens_ids):
	'''Декодирование последовательности токенов'''
	code_bert_decoded = tokenizer_code_bert.decode(tokens_ids)
	print(f"Декодированная строка: {code_bert_decoded}")
	
class Code2TestDataset(Dataset):
	'''Класс датасет для задачи генерации тестов'''

	def __init__(self, code_dataset, tokenizer_code_bert, tokenizer_gpt, max_length=512):
		'''
		Конструктор датасета

		Параметры:
		- code_dataset: датасет pd.DataFrame
		- tokenizer_code_bert: токенизатор code_bert
		- tokenizer_gpt: токенизатор gpt
		- max_length: максимальная длина последовательности (default: 512)
		'''
		self.code_dataset = code_dataset
		self.tokenizer_code_bert = tokenizer_code_bert
		self.tokenizer_gpt = tokenizer_gpt
		self.max_length = max_length

	def __getitem__(self, idx, idx_to_token=False):
		'''
		Get-метод - возвращает сэмпл по индексу

		Параметры:
		- idx: индекс
		- idx_to_token: флаг для отображения токенов из индексов (default: False)
		'''
		focal_method_input = self.code_dataset.at[idx, 'input_string_focal_method']
		focal_cls_input = self.code_dataset.at[idx, 'input_string_focal_cls']
		response = self.code_dataset.at[idx, 'response']

		def encode_text(text, tokenizer):
			encoding = tokenizer.encode_plus(
				text,
				add_special_tokens=True,
				max_length=self.max_length if tokenizer == self.tokenizer_code_bert else self.max_length * 2,
				padding='max_length',
				truncation=True,
				return_attention_mask=True,
				return_tensors='pt',
			)
			input_ids = encoding['input_ids'].flatten()
			attention_mask = encoding['attention_mask'].flatten()
			return input_ids, attention_mask

		input_ids_focal_method, attention_mask_focal_method = encode_text(focal_method_input, self.tokenizer_code_bert)
		input_ids_focal_cls, attention_mask_focal_cls = encode_text(focal_cls_input, self.tokenizer_code_bert)
		input_ids_response, attention_mask_response = encode_text(response, self.tokenizer_gpt)

		if idx_to_token:
			return {
				'input_ids_focal_method': self.tokenizer_code_bert.convert_ids_to_tokens(input_ids_focal_method),
				'attention_mask_focal_method': attention_mask_focal_method,
				'input_ids_focal_cls': self.tokenizer_code_bert.convert_ids_to_tokens(input_ids_focal_cls),
				'attention_mask_focal_cls': attention_mask_focal_cls,
				'ids_response': self.tokenizer_gpt.convert_ids_to_tokens(input_ids_response),
				'attention_mask_response': attention_mask_response
			}
		return {
			'input_ids_focal_method': input_ids_focal_method,
			'attention_mask_focal_method': attention_mask_focal_method,
			'input_ids_focal_cls': input_ids_focal_cls,
			'attention_mask_focal_cls': attention_mask_focal_cls,
			'ids_response': input_ids_response,
			'attention_mask_response': attention_mask_response
		}
	
	def __len__(self):
		'''Функция возвращает длину датасета. В качестве длины берется размер датасета по axis = 0'''
		return self.code_dataset.shape[0]


def get_datasets(data, 
				dataset_cls = Code2TestDataset,
				max_length = 512,
				tokenizer = tokenizer_code_bert,
				train_size = 0.7):
	'''
	Функция get_datasets() возвращает train и val датасеты на основе конструктора AccentDataset, делая train_val_spilt
	
	Параметры:
	-dataset_cls: класс датасета, конструктор которого будет вызываться (default: Code2TestDataset)
	-max_length: максимальная статья последовательности токенов
	-data: датасает pd.DataFrame
	-tokenizer: токенизатор (default: tokenizer_code_bert)
	-train_size: размер тренировочной выборки (default: 0.7)
	
	'''
	
	dataset = dataset_cls(code_dataset = data,
					   	tokenizer = tokenizer,
						max_length=max_length)
	
	train_size = int(train_size * len(dataset))
	val_size = len(dataset) - train_size
	train_dataset, test_dataset = random_split(dataset, [train_size, val_size])

	return train_dataset, test_dataset

def get_loaders(train_dataset,
			val_dataset,
			shuffle_train = True,
			shuffle_val = False,
			batch_size = 32):
	
	'''
	Функция get_loaders() для получения train, val даталоадеров

	Параметры:
	-train_dataset: тренировочный датасет
	-val_dataset: валидационный датасет
	-shuffle_train: флаг перемешивания для train (default: True)
	-shuffle_val: флаг перемешивания для val (default: False)
	-batch_size: размер батча данных (default: 32)
	'''
	
	# train_dataloader
	train_dataloader = DataLoader(
			train_dataset,   
			batch_size = batch_size,
			shuffle = shuffle_train,
		)

	# validation_dataloader
	validation_dataloader = DataLoader(
			val_dataset, 
			batch_size = batch_size,
			shuffle = shuffle_val,
		)
	
	# Возвращаем даталоадеры
	return train_dataloader, validation_dataloader

class LargeCodeModel(nn.Module):
	'''Класс для сложной языковой модели, которая обрабатывает входной код'''
	def __init__(self, bert_model_name, gpt2_name):
		super(LargeCodeModel, self).__init__()
		
		self.bert1 = AutoModel.from_pretrained(bert_model_name, output_hidden_states= True)
		self.bert2 = AutoModel.from_pretrained(bert_model_name, output_hidden_states= True)
		self.tokenizer_code_bert = AutoTokenizer.from_pretrained(bert_model_name)

		self.new_special_tokens = ['<FUNC_TOKEN>',
            '<INFO_TOKEN>',
            '<CLS_TOKEN>', 
            '<AST_TOKEN>', 
            '<DESCRIPTION_TOKEN>',
            '<COMMENTS_TOKEN>']

		self.special_tokens_dict = {
			'additional_special_tokens': new_special_tokens
		}

		self.tokenizer_code_bert.add_special_tokens(self.special_tokens_dict)
		self.bert1.resize_token_embeddings(len(self.tokenizer_code_bert))
		self.bert2.resize_token_embeddings(len(self.tokenizer_code_bert))

		self.gpt2_config = AutoConfig.from_pretrained(gpt2_name, is_decoder=True, add_cross_attention= True)
		self.gpt2_config.add_cross_attention = True  # Включение cross-attention
		self.tokenizerGPT = AutoTokenizer.from_pretrained(gpt2_name)
		self.tokenizerGPT.add_special_tokens({'pad_token': '<PAD>'})
		self.gpt2 = GPT2LMHeadModel.from_pretrained(modelGPT2Path, config=config)
		self.gpt2.resize_token_embeddings(len(self.tokenizerGPT))

		self.batch_norm = nn.BatchNorm1d(self.bert1.config.hidden_size)

		self.projection = nn.Linear(
            self.bert1.config.hidden_size + self.bert2.config.hidden_size,
            self.gpt2.config.hidden_size
        )

	# forward call
	def forward(self, focal_method_input_ids, 
			 			focal_method_attention_masks, 
						focal_cls_input_ids,
						focal_cls_attention_masks,
						response_ids, response_attention_masks):
		
		bert1_outputs = self.bert1(focal_method_input_ids, focal_method_attention_masks)
		last_hidden_state_bert1 = bert1_outputs['last_hidden_state']

		bert2_outputs = self.bert2(focal_cls_input_ids, focal_cls_attention_masks)
		last_hidden_state_bert2 = bert2_outputs['last_hidden_state']

		# print(last_hidden_state_bert1.size())
		# print(last_hidden_state_bert2.size())

		concat_hidden_states = torch.cat([last_hidden_state_bert1, last_hidden_state_bert2], dim=1)

		# print(concat_hidden_states.size())

		# Для BatchNorm
		batch_norm_input = concat_hidden_states.view(-1, 768)
		normalized_hidden_states = self.batch_norm(batch_norm_input)
		normalized_hidden_states = normalized_hidden_states.view(2, 1024, 768)
		# print(normalized_hidden_states.size())
		# print(torch.cat([focal_method_attention_masks, focal_cls_attention_masks], dim=1).size())
		# print(response_ids.size())
		# print(response_input_mask.size())
		
		gpt2_outputs = self.gpt2(
            input_ids=response_ids,
            attention_mask=response_attention_masks,
            encoder_hidden_states=normalized_hidden_states,
            encoder_attention_mask=torch.cat([focal_method_attention_masks, focal_cls_attention_masks], dim=1),
			labels=response_ids
        )

		return gpt2_outputs

		

