from .base_model import BaseModel
from .resnet_model import ResNet50Model
from .vgg_model import VGG16Model

class ModelFactory:
    """Фабрика для создания моделей"""
    
    AVAILABLE_MODELS = {
        'ResNet50': ResNet50Model,
        'VGG16': VGG16Model,
    }
    
    @classmethod
    def create_model(cls, model_name: str, weights: str = 'imagenet') -> BaseModel:
        """Создать модель по имени"""
        if model_name not in cls.AVAILABLE_MODELS:
            raise ValueError(f"Неизвестная модель: {model_name}")
        
        model_class = cls.AVAILABLE_MODELS[model_name]
        model = model_class(weights)
        model.load()
        return model
    
    @classmethod
    def get_available_models(cls) -> list:
        """Получить список доступных моделей"""
        return list(cls.AVAILABLE_MODELS.keys())
    