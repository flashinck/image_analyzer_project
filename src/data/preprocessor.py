import cv2
import numpy as np

class ImagePreprocessor:
    '''Предварительная обработка изображений'''
    
    def __init__(self, model_name: str = "ResNet50"):
        self.model_name = model_name
        self._load_preprocessing_params()
    
    def _load_preprocessing_params(self):
        '''Загрузить параметры нормализации для модели'''
        self.preprocessing_params = {
            'ResNet50': {
                'mean': [0.485, 0.456, 0.406],
                'std': [0.229, 0.224, 0.225],
                'size': (224, 224)
            },
            'VGG16': {
                'mean': [0.485, 0.456, 0.406],
                'std': [0.229, 0.224, 0.225],
                'size': (224, 224)
            },
            'EfficientNet': {
                'mean': [0.485, 0.456, 0.406],
                'std': [0.229, 0.224, 0.225],
                'size': (256, 256)
            }
        }
    
    def preprocess(self, image: np.ndarray) -> np.ndarray:
        '''Полная предварительная обработка'''
        params = self.preprocessing_params[self.model_name]
        
        resized = cv2.resize(image, params['size'])
        normalized = resized.astype('float32') / 255.0
        
        for i, (mean, std) in enumerate(zip(params['mean'], params['std'])):
            normalized[:, :, i] = (normalized[:, :, i] - mean) / std
        
        batch = np.expand_dims(normalized, axis=0)
        return batch
