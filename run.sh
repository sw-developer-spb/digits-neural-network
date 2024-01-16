#!/bin/bash

# Путь к активационному скрипту виртуального окружения
venv_activate="venv/bin/activate"

# Проверка существования виртуального окружения
if [ -f "$venv_activate" ]; then
    # Активация виртуального окружения
    source "$venv_activate"
    
    # Здесь можно добавить выполнение вашего Python-скрипта
    python main.py
else
    echo "Виртуальное окружение не найдено."
fi
