"""
Модуль тестирования

Содержит unit-тесты и интеграционные тесты для проекта.
"""

# Указываем, что это пакет с тестами
__all__ = [
    "test_analysis",
    "test_data", 
    "test_models",
    "test_integration"
]

# Конфигурация тестов
TEST_CONFIG = {
    "test_data_dir": "test_data",
    "test_images_count": 10,
    "timeout_seconds": 60
}

def setup_test_environment():
    """Настройка окружения для тестирования"""
    import os
    import sys
    
    # Добавляем src в путь для импорта
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    
    # Создаем директорию для тестовых данных
    test_data_dir = os.path.join(os.path.dirname(__file__), "test_data")
    os.makedirs(test_data_dir, exist_ok=True)
    
    print(f"Настройка тестового окружения завершена. Данные в: {test_data_dir}")

# Автоматическая настройка при импорте в тестовом окружении
if "pytest" in sys.modules:
    setup_test_environment()