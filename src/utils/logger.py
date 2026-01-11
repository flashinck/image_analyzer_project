import logging
import sys
from datetime import datetime

def setup_logger(name: str, level=logging.INFO):
    """Настройка логгера"""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Форматтер
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler
    file_handler = logging.FileHandler(f'logs/image_analyzer_{datetime.now().strftime("%Y%m%d")}.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger

# Глобальный логгер
logger = setup_logger('image_analyzer')