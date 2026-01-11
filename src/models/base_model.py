from abc import ABC, abstractmethod
import tensorflow as tf
import numpy as np
import time

class BaseModel(ABC):
    """Базовый класс для всех моделей"""
    
    def __init__(self, name: str, weights: str = 'imagenet'):
        self.name = name
        self.weights = weights
        self.model = None
        self.device = 'CPU'
    
    @abstractmethod
    def load(self):
        """Загрузить модель"""
        pass
    
    @abstractmethod
    def predict(self, image: np.ndarray) -> dict:
        """Предсказать класс"""
        pass
    
    def set_device(self, device: str):
        """Установить устройство (CPU/GPU)"""
        self.device = device
        if device == 'GPU':
            gpus = tf.config.list_physical_devices('GPU')
            if gpus:
                tf.config.set_visible_devices(gpus[0], 'GPU')
    
    def get_model_info(self) -> dict:
        """Получить информацию о модели"""
        return {
            'name': self.name,
            'weights': self.weights,
            'device': self.device,
            'loaded': self.model is not None
        }
