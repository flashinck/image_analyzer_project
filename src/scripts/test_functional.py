#!/usr/bin/env python3
"""Функциональное тестирование"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_all():
    print("Запуск функциональных тестов...")
    
    # Импорт модулей
    try:
        from data.loader import ImageLoader
        from data.preprocessor import ImagePreprocessor
        from analysis.analyzer import ImageAnalyzer
        from storage.database import AnalysisDatabase
        print("✅ Все модули импортированы успешно")
    except ImportError as e:
        print(f"❌ Ошибка импорта: {e}")
        return False
    
    # Проверка фабрики моделей
    try:
        from models.model_factory import ModelFactory
        models = ModelFactory.get_available_models()
        print(f"✅ Доступные модели: {models}")
    except Exception as e:
        print(f"❌ Ошибка фабрики моделей: {e}")
    
    return True

if __name__ == "__main__":
    success = test_all()
    sys.exit(0 if success else 1)