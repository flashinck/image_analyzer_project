import re
from pathlib import Path
from urllib.parse import urlparse

class Validators:
    """Класс для валидации данных"""
    
    @staticmethod
    def validate_image_file(file_path: Path) -> bool:
        """Валидация файла изображения"""
        if not file_path.exists():
            return False
        
        if file_path.stat().st_size > 50 * 1024 * 1024:  # 50 МБ
            return False
        
        valid_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.webp'}
        return file_path.suffix.lower() in valid_extensions
    
    @staticmethod
    def validate_url(url: str) -> bool:
        """Валидация URL"""
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except:
            return False
    
    @staticmethod
    def validate_model_name(model_name: str) -> bool:
        """Валидация имени модели"""
        valid_models = {'ResNet50', 'VGG16', 'EfficientNetB0'}
        return model_name in valid_models