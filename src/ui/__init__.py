"""
Модуль графического интерфейса

Реализация GUI на PyQt5 для взаимодействия с пользователем.
"""

from .gui import ImageAnalyzerGUI, main

__all__ = ["ImageAnalyzerGUI", "main"]

# Конфигурация интерфейса
UI_CONFIG = {
    "window_title": "Image Analyzer - Анализ изображений",
    "window_size": (1200, 800),
    "supported_languages": ["ru", "en"],
    "default_language": "ru",
    "theme": "default",
    "font_size": 10
}

def get_ui_config() -> dict:
    """Получить конфигурацию интерфейса"""
    return UI_CONFIG.copy()

def run_gui():
    """Запустить графический интерфейс"""
    return main()