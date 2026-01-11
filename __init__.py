"""
Image Analyzer Project
Курсовой проект: Программа для анализа изображений с использованием ИНС

Основной пакет проекта.
"""

__version__ = "1.0.0"
__author__ = "Владислав"
__email__ = "ваш.email@example.com"
__description__ = "Программа для анализа изображений с использованием искусственной нейронной сети"

# Экспорт для удобного доступа
import sys
import os

# Добавляем src в путь Python для импорта
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def get_project_info() -> dict:
    """Получить информацию о проекте"""
    return {
        "name": "Image Analyzer Project",
        "version": __version__,
        "author": __author__,
        "email": __email__,
        "description": __description__,
        "python_version": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    }

def setup_project():
    """Настройка проекта (создание необходимых директорий)"""
    import os
    
    # Создаем необходимые директории
    directories = ['logs', 'data', 'models']
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Создана директория: {directory}")
    
    print("Настройка проекта завершена!")

# Автоматическая настройка при импорте
if __name__ != "__main__":
    setup_project()