# Используем официальный образ Python 3.12
FROM python:3.12-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Обновляем пакеты в базовом образе
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Копируем зависимости проекта в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY LLM .

# Указываем команду для запуска приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
