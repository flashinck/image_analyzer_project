"""
Модуль работы с данными

Содержит классы для загрузки, валидации и предварительной обработки изображений.
"""

from .loader import ImageLoader
from .preprocessor import ImagePreprocessor

__all__ = ["ImageLoader", "ImagePreprocessor"]

# Конфигурация данных
DATA_CONFIG = {
    "supported_formats": ['.jpg', '.jpeg', '.png', '.bmp', '.webp'],
    "max_file_size_mb": 50,
    "default_image_size": (224, 224),
    "normalization_means": [0.485, 0.456, 0.406],
    "normalization_stds": [0.229, 0.224, 0.225]
}

def get_supported_formats() -> list:
    """Получить список поддерживаемых форматов"""
    return DATA_CONFIG["supported_formats"].copy()

def get_data_config() -> dict:
    """Получить конфигурацию данных"""
    return DATA_CONFIG.copy()