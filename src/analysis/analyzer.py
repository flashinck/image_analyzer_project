from datetime import datetime
import logging
from ..data.loader import ImageLoader
from ..data.preprocessor import ImagePreprocessor
from ..models.model_factory import ModelFactory

class ImageAnalyzer:
    """Главный класс для анализа изображений"""
    
    def __init__(self, model_name: str = 'ResNet50'):
        self.model = ModelFactory.create_model(model_name)
        self.preprocessor = ImagePreprocessor(model_name)
        self.logger = logging.getLogger(__name__)
        self.health_status = {
            'status': 'healthy',
            'model_loaded': True,
            'last_check': datetime.now().isoformat()
        }
    
    def analyze(self, image_path: str, top_k: int = 5) -> dict:
        """Полный анализ изображения"""
        
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
        
        self.logger.info(f"Анализ завершен. Top-1: {predictions['predictions'][0]['class']}")
        return analysis_result
    
    def health_check(self) -> dict:
        """Проверка состояния анализатора"""
        self.health_status['last_check'] = datetime.now().isoformat()
        try:
            # Простая проверка модели
            test_input = self.preprocessor.preprocess(
                np.zeros((224, 224, 3), dtype=np.uint8)
            )
            _ = self.model.predict(test_input, top_k=1)
            self.health_status['status'] = 'healthy'
        except Exception as e:
            self.health_status['status'] = 'unhealthy'
            self.health_status['error'] = str(e)
        
        return self.health_status
    
    def get_model_info(self) -> dict:
        """Получить информацию о текущей модели"""
        return self.model.get_model_info()