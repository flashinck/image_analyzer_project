from datetime import datetime
from src.data.loader import ImageLoader
from src.data.preprocessor import ImagePreprocessor
from src.models.model_factory import ModelFactory
import logging

class ImageAnalyzer:
    '''Главный класс для анализа изображений'''
    
    def __init__(self, model_name: str = 'ResNet50'):
        self.model = ModelFactory.create_model(model_name)
        self.preprocessor = ImagePreprocessor(model_name)
        self.logger = logging.getLogger(__name__)
    
    def analyze(self, image_path: str, top_k: int = 5) -> dict:
        '''Полный анализ изображения'''
        
        loader = ImageLoader()
        if image_path.startswith('http'):
            image = loader.load_from_url(image_path)
        else:
            image = loader.load_from_file(image_path)
        
        original_shape = image.shape
        processed = self.preprocessor.preprocess(image)
        predictions = self.model.predict(processed, top_k=top_k)
        
        analysis_result = {
            'file': image_path,
            'original_shape': original_shape,
            'processed_shape': processed.shape,
            'predictions': predictions['predictions'],
            'inference_time': predictions['inference_time'],
            'model': predictions['model'],
            'device': predictions['device'],
            'timestamp': datetime.now().isoformat()
        }
        
        self.logger.info(f"Анализ завершен. Top-1: {predictions['predictions']['class']}")
        return analysis_result
