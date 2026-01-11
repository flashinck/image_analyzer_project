import pytest
import numpy as np
from src.models.model_factory import ModelFactory

class TestResNet50Model:
    '''Тесты для ResNet50 модели'''
    
    @pytest.fixture
    def model(self):
        return ModelFactory.create_model('ResNet50')
    
    def test_model_load(self, model):
        '''Тест загрузки модели'''
        assert model.model is not None
        assert model.name == 'ResNet50'
    
    def test_model_predict_shape(self, model):
        '''Тест формы вывода предсказания'''
        image = np.random.randn(1, 224, 224, 3).astype(np.float32)
        result = model.predict(image)
        
        assert 'predictions' in result
        assert 'inference_time' in result
        assert len(result['predictions']) <= 5
    
    def test_model_device_setting(self, model):
        '''Тест установки устройства'''
        model.set_device('CPU')
        assert model.device == 'CPU'
        
        model.set_device('GPU')
        assert model.device == 'GPU'
