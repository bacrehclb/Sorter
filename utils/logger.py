import logging
import os
import sys
from datetime import datetime

def setup_logger(log_file= "logs/sorter.log"):
    # Создание папки для логов
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    #Настройка форматирования
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'
    #Настройки корневого логера
    logging.basicConfig(
                        level=logging.INFO,
                        format=log_format,
                        datefmt=date_format,
                        handlers=[
                        logging.FileHandler(log_file, encoding="utf-8"),
                        logging.StreamHandler(sys.stdout)])
    return logging.getLogger(__name__)

# Функция для ротации логов (чтобы файл не разрастался)
def rotate_logs(log_file= "logs/sorter.log", max_size_mb=10, backup_count=5):
    #Проверка на превышение размера(10мб)
    if os.path.exists(log_file):
        size_mb = os.path.getsize(log_file) / (1024 * 1024)
        if size_mb > max_size_mb:
            time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            backup_name = f"{log_file}.{time_stamp}.bak"
            os.rename(log_file, backup_name)
            #удаление старых бэкапов
            backups = sorted([f for f in os.listdir(os.path.dirname(log_file))])
            while len(backups) > backup_count:
                os.remove(os.path.join(os.path.dirname(log_file), backups.pop(0)))