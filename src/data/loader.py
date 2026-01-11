from pathlib import Path
from typing import Union
from PIL import Image
import numpy as np
import logging

class ImageLoader:
    '''Загрузчик изображений из различных источников'''
    
    SUPPORTED_FORMATS = {'.jpg', '.jpeg', '.png', '.bmp', '.webp'}
    MAX_FILE_SIZE = 50 * 1024 * 1024
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def load_from_file(self, file_path: Union[str, Path]) -> np.ndarray:
        '''Загрузить изображение из файла'''
        file_path = Path(file_path)
        self._validate_file(file_path)
        
        img = Image.open(file_path).convert('RGB')
        img_array = np.array(img)
        
        self.logger.info(f"Загружено изображение: {file_path}")
        return img_array
    
    def load_from_url(self, url: str) -> np.ndarray:
        '''Загрузить изображение по URL'''
        import requests
        from io import BytesIO
        
        try:
            response = requests.get(url, timeout=10, stream=True)
            response.raise_for_status()
            
            content_length = response.headers.get('content-length')
            if content_length and int(content_length) > self.MAX_FILE_SIZE:
                raise ValueError("Файл слишком большой")
            
            img = Image.open(BytesIO(response.content)).convert('RGB')
            img_array = np.array(img)
            
            self.logger.info(f"Загружено изображение: {url}")
            return img_array
        except Exception as e:
            self.logger.error(f"Ошибка загрузки URL: {e}")
            raise
    
    def _validate_file(self, file_path: Path) -> None:
        '''Валидировать файл'''
        if not file_path.exists():
            raise FileNotFoundError(f"Файл не найден: {file_path}")
        
        if file_path.suffix.lower() not in self.SUPPORTED_FORMATS:
            raise ValueError(f"Неподдерживаемый формат: {file_path.suffix}")
        
        if file_path.stat().st_size > self.MAX_FILE_SIZE:
            raise ValueError("Файл слишком большой")
