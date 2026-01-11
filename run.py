#!/usr/bin/env python3
"""Точка входа для приложения"""
import sys
import os

# Добавляем src в путь
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def main():
    """Основная функция запуска"""
    try:
        from ui.gui import main as gui_main
        print("Запуск Image Analyzer GUI...")
        gui_main()
    except ImportError as e:
        print(f"Ошибка импорта: {e}")
        print("Убедитесь, что все зависимости установлены:")
        print("pip install -r requirements.txt")
        return 1
    except Exception as e:
        print(f"Ошибка запуска: {e}")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())