"""
Модуль анализа изображений

Координирует процесс загрузки, обработки и классификации изображений.
"""

from .analyzer import ImageAnalyzer

__all__ = ["ImageAnalyzer"]

# Конфигурация анализа
ANALYSIS_CONFIG = {
    "default_top_k": 5,
    "min_confidence": 0.01,
    "timeout_seconds": 30,
    "batch_size": 1,
    "supported_devices": ["CPU", "GPU"]
}

def get_analysis_config() -> dict:
    """Получить конфигурацию анализа"""
    return ANALYSIS_CONFIG.copy()

def create_analyzer(model_name: str = "ResNet50") -> "ImageAnalyzer":
    """Создать анализатор с указанной моделью"""
    return ImageAnalyzer(model_name)