"""
Основной пакет исходного кода Image Analyzer

Содержит все модули для анализа изображений с использованием нейронных сетей.
"""

__all__ = ["models", "data", "analysis", "storage", "ui", "utils"]

from . import models
from . import data
from . import analysis
from . import storage
from . import ui
from . import utils

# Версия пакета
__version__ = "1.0.0"

def init_package():
    """Инициализация пакета"""
    import logging
    from .utils.logger import setup_logger
    
    # Настройка логгера
    logger = setup_logger("image_analyzer")
    logger.info(f"Инициализация Image Analyzer v{__version__}")
    
    return logger

# Автоматическая инициализация при импорте
if __name__ != "__main__":
    logger = init_package()