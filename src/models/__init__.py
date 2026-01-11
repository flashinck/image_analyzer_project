"""
Модуль моделей нейронных сетей

Содержит реализации различных архитектур нейронных сетей для классификации изображений.
"""

from .base_model import BaseModel
from .resnet_model import ResNet50Model
from .vgg_model import VGG16Model
from .model_factory import ModelFactory

__all__ = [
    "BaseModel",
    "ResNet50Model",
    "VGG16Model",
    "ModelFactory"
]

# Конфигурация моделей
MODEL_CONFIG = {
    "available_models": ["ResNet50", "VGG16"],
    "default_model": "ResNet50",
    "default_weights": "imagenet",
    "supported_backends": ["tensorflow", "pytorch"]
}

def get_available_models() -> list:
    """Получить список доступных моделей"""
    return MODEL_CONFIG["available_models"].copy()

def get_model_config() -> dict:
    """Получить конфигурацию моделей"""
    return MODEL_CONFIG.copy()