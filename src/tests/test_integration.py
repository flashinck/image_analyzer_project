"""Интеграционные тесты"""
import pytest
import tempfile
import os
from PIL import Image
import numpy as np

class TestIntegration:
    """Тесты интеграции компонентов"""
    
    def test_complete_flow(self):
        """Тест полного потока: загрузка → обработка → анализ"""
        from data.loader import ImageLoader
        from data.preprocessor import ImagePreprocessor
        from analysis.analyzer import ImageAnalyzer
        
        # Создание тестового изображения
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp:
            img = Image.new('RGB', (224, 224), color='red')
            img.save(tmp.name, 'JPEG')
            
            # Загрузка
            loader = ImageLoader()
            image = loader.load_from_file(tmp.name)
            assert image.shape == (224, 224, 3)
            
            # Предобработка
            preprocessor = ImagePreprocessor('ResNet50')
            processed = preprocessor.preprocess(image)
            assert processed.shape == (1, 224, 224, 3)
            
            # Анализ
            analyzer = ImageAnalyzer('ResNet50')
            result = analyzer.analyze(tmp.name)
            
            assert 'predictions' in result
            assert len(result['predictions']) > 0
            assert 'inference_time' in result
            
            os.unlink(tmp.name)
    
    def test_database_integration(self):
        """Тест интеграции с БД"""
        from storage.database import AnalysisDatabase
        import tempfile
        
        with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as tmp:
            db = AnalysisDatabase(tmp.name)
            
            # Тестовые данные
            test_data = {
                'file': 'test.jpg',
                'model': 'ResNet50',
                'predictions': [{'class': 'cat', 'probability': 0.95}],
                'inference_time': 0.1,
                'device': 'CPU'
            }
            
            # Сохранение
            db.save_analysis(test_data)
            
            # Получение истории
            history = db.get_history()
            assert len(history) == 1
            
            os.unlink(tmp.name)