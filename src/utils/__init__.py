"""
Модуль вспомогательных утилит

Содержит общие функции для логирования, валидации и других задач.
"""

from .logger import setup_logger, logger
from .validators import Validators

__all__ = ["setup_logger", "logger", "Validators"]

# Дополнительные утилиты
import os
import sys
from pathlib import Path

def get_project_root() -> Path:
    """Получить путь к корню проекта"""
    # От utils/ поднимаемся на 2 уровня вверх
    return Path(__file__).resolve().parent.parent.parent

def get_absolute_path(relative_path: str) -> str:
    """Получить абсолютный путь относительно корня проекта"""
    return os.path.join(get_project_root(), relative_path)

def ensure_directory(path: str) -> str:
    """Создать директорию если не существует"""
    os.makedirs(path, exist_ok=True)
    return path

# Автоматически создаем необходимые директории
if __name__ != "__main__":
    # Создаем директорию для логов если её нет
    log_dir = get_absolute_path("logs")
    ensure_directory(log_dir)