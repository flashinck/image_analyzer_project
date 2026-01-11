"""
Пакет скриптов для различных задач

Содержит вспомогательные скрипты для тестирования, развертывания и мониторинга.
"""

__all__ = ["test_functional"]

from .test_functional import test_all

def run_all_scripts():
    """Запустить все скрипты"""
    print("Запуск скриптов проекта Image Analyzer...")
    
    results = {}
    
    try:
        from .test_functional import test_all as functional_test
        results["functional_test"] = functional_test()
    except Exception as e:
        results["functional_test"] = f"Ошибка: {e}"
    
    return results

if __name__ == "__main__":
    run_all_scripts()