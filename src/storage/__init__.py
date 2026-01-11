"""
Модуль хранения данных

Управление базой данных, историей анализов и экспортом результатов.
"""

from .database import AnalysisDatabase
from .exporter import ResultsExporter

__all__ = ["AnalysisDatabase", "ResultsExporter"]

# Конфигурация хранилища
STORAGE_CONFIG = {
    "default_db_name": "analysis_history.db",
    "default_table_name": "analyses",
    "max_history_entries": 1000,
    "export_formats": ["json", "csv", "txt"],
    "backup_enabled": True,
    "backup_interval_days": 7
}

def get_storage_config() -> dict:
    """Получить конфигурацию хранилища"""
    return STORAGE_CONFIG.copy()

def create_database(db_path: str = None) -> "AnalysisDatabase":
    """Создать объект базы данных"""
    return AnalysisDatabase(db_path)