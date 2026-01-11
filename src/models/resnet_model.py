from src.models.base_model import BaseModel
import tensorflow as tf
import time

class ResNet50Model(BaseModel):
    '''ResNet50 модель для классификации'''
    
    def __init__(self, weights: str = 'imagenet'):
        super().__init__('ResNet50', weights)
    
    def load(self):
        '''Загрузить предварительно обученную модель'''
        from tensorflow.keras.applications import ResNet50
        from tensorflow.keras.applications.resnet50 import decode_predictions
        
        self.model = ResNet50(weights=self.weights)
        self.decode_predictions = decode_predictions
    
    def predict(self, image, top_k: int = 5) -> dict:
        '''Предсказать класс изображения'''
        start_time = time.time()
        
        predictions = self.model.predict(image, verbose=0)
        decoded = self.decode_predictions(predictions, top=top_k)
        
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

