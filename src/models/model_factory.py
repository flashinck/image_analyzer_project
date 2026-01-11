from src.models.base_model import BaseModel
from src.models.resnet_model import ResNet50Model

class ModelFactory:
    '''Фабрика для создания моделей'''
    
    AVAILABLE_MODELS = {
        'ResNet50': ResNet50Model,
        'VGG16': lambda w: VGG16Model(w),
        'EfficientNetB0': lambda w: EfficientNetB0Model(w),
    }
    
    @classmethod
    def create_model(cls, model_name: str, weights: str = 'imagenet') -> BaseModel:
        '''Создать модель по имени'''
        if model_name not in cls.AVAILABLE_MODELS:
            raise ValueError(f"Неизвестная модель: {model_name}")
        
        model = cls.AVAILABLE_MODELS[model_name](weights)
        model.load()
        return model
