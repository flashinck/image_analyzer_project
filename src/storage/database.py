import sqlite3
from datetime import datetime

class AnalysisDatabase:
    '''Управление историей анализов'''
    
    def __init__(self, db_path: str = 'analysis_history.db'):
        self.db_path = db_path
        self._init_db()
    
    def _init_db(self):
        '''Инициализировать базу данных'''
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS analyses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    file_path TEXT NOT NULL,
                    model_name TEXT NOT NULL,
                    top1_class TEXT NOT NULL,
                    top1_probability REAL NOT NULL,
                    inference_time REAL NOT NULL,
                    device TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
    
    def save_analysis(self, analysis_result: dict):
        '''Сохранить результат анализа'''
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO analyses 
                (file_path, model_name, top1_class, top1_probability, 
                 inference_time, device)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                analysis_result['file'],
                analysis_result['model'],
                analysis_result['predictions']['class'],
                analysis_result['predictions']['probability'],
                analysis_result['inference_time'],
                analysis_result['device']
            ))
            conn.commit()
    
    def get_history(self, limit: int = 100) -> list:
        '''Получить историю анализов'''
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT * FROM analyses ORDER BY timestamp DESC LIMIT ?',
                (limit,)
            )
            return cursor.fetchall()
