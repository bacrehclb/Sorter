import config
import json
import os
import platform

# возвращает строку полный путь к файлу config.json где будут храниться настройки пользователя
def get_config_path():
    home_path = os.path.expanduser("~")
    this_platform = platform.system()
    if this_platform == "Windows":
        config_dir = os.path.join(home_path, "AppData", "Roaming", "Sorter")
    elif this_platform == "Darwin":
        config_dir = os.path.join(home_path, "Library", "Application Support" "Sorter")
    else:
        config_dir = os.path.join(home_path, ".config", "sorter")
    os.makedirs(config_dir, exist_ok=True)
    return os.path.join(config_dir, "config.json")

# возвращаем путь к файлу default_cfg.json из директории config
def load_default_config_path():
    this_path = os.path.dirname(__file__)
    uplvl_path = os.path.dirname(this_path)
    return os.path.join(uplvl_path, "config/default_cfg.json")

#
# def load_default_config(default_cfg_file):



