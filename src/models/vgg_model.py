import tensorflow as tf
import numpy as np
import time
from .base_model import BaseModel

class VGG16Model(BaseModel):
    """VGG16 модель для классификации"""
    
    def __init__(self, weights: str = 'imagenet'):
        super().__init__('VGG16', weights)
        self.decode_predictions = None
    
    def load(self):
        """Загрузить предварительно обученную модель"""
        from tensorflow.keras.applications import VGG16
        from tensorflow.keras.applications.vgg16 import decode_predictions
        
        self.model = VGG16(weights=self.weights)
        self.decode_predictions = decode_predictions
    
    def predict(self, image: np.ndarray, top_k: int = 5) -> dict:
        """Предсказать класс изображения"""
        start_time = time.time()
        
        predictions = self.model.predict(image, verbose=0)
        decoded = self.decode_predictions(predictions, top=top_k)[0]
        
        inference_time = time.time() - start_time
        
        return {
            'model': self.name,
            'predictions': [
                {
                    'class': label,
                    'probability': float(prob),
                    'percentage': float(prob) * 100
                }
                for (code, label, prob) in decoded
            ],
            'inference_time': inference_time,
            'device': self.device
        }