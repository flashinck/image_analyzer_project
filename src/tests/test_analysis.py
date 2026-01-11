import pytest
from src.analysis.analyzer import ImageAnalyzer
from src.storage.database import AnalysisDatabase
from PIL import Image

class TestImageAnalyzer:
    '''Integration-тесты для анализатора'''
    
    @pytest.fixture
    def analyzer(self):
        return ImageAnalyzer('ResNet50')
    
    @pytest.fixture
    def database(self, tmp_path):
        return AnalysisDatabase(tmp_path / 'test.db')
    
    def test_analyze_and_save(self, analyzer, database, tmp_path):
        '''Тест анализа и сохранения результатов'''
        img = Image.new('RGB', (224, 224), color='green')
        img_path = tmp_path / "test.jpg"
        img.save(img_path)
        
        result = analyzer.analyze(str(img_path))
        database.save_analysis(result)
        
        history = database.get_history()
        assert len(history) > 0
    
    def test_analysis_result_structure(self, analyzer, tmp_path):
        '''Тест структуры результата анализа'''
        img = Image.new('RGB', (224, 224), color='blue')
        img_path = tmp_path / "test.jpg"
        img.save(img_path)
        
        result = analyzer.analyze(str(img_path))
        
        assert 'file' in result
        assert 'predictions' in result
        assert 'inference_time' in result
        assert 'model' in result
        assert 'timestamp' in result
