import pytest
import numpy as np
from PIL import Image
from src.data.loader import ImageLoader
from src.data.preprocessor import ImagePreprocessor

class TestImageLoader:
    '''Тесты для класса ImageLoader'''
    
    @pytest.fixture
    def loader(self):
        return ImageLoader()
    
    def test_load_valid_image(self, loader, tmp_path):
        '''Тест загрузки валидного изображения'''
        img = Image.new('RGB', (224, 224), color='red')
        img_path = tmp_path / "test.jpg"
        img.save(img_path)
        
        loaded = loader.load_from_file(img_path)
        assert loaded.shape == (224, 224, 3)
    
    def test_load_nonexistent_file(self, loader):
        '''Тест загрузки несуществующего файла'''
        with pytest.raises(FileNotFoundError):
            loader.load_from_file('/nonexistent/path/image.jpg')


class TestImagePreprocessor:
    '''Тесты для класса ImagePreprocessor'''
    
    @pytest.fixture
    def preprocessor(self):
        return ImagePreprocessor()
    
    def test_preprocess_shape(self, preprocessor):
        '''Тест формы обработанного изображения'''
        image = np.random.randint(0, 256, (400, 300, 3), dtype=np.uint8)
        processed = preprocessor.preprocess(image)
        assert processed.shape == (1, 224, 224, 3)
    
    def test_preprocess_value_range(self, preprocessor):
        '''Тест диапазона значений обработанного изображения'''
        image = np.random.randint(0, 256, (400, 300, 3), dtype=np.uint8)
        processed = preprocessor.preprocess(image)
        assert processed.min() < 0
        assert processed.max() < 3
