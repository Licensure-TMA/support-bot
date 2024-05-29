# Используем официальный образ Python 3.9 в качестве базового
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл requirements.txt в рабочую директорию
COPY requirements.txt .

# Устанавливаем зависимости Python из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы бота в рабочую директорию
COPY . .

# Определяем переменную окружения для запуска бота
ENV PYTHONUNBUFFERED=1

# Указываем команду для запуска бота
CMD ["python", "main.py"]