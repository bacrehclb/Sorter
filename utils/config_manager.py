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
def get_default_config_path():
    this_path = os.path.dirname(__file__)
    uplvl_path = os.path.dirname(this_path)
    return os.path.join(uplvl_path, "config/default_cfg.json")

# открывает и читает default_cfg и возвращает словарь с настройками по умолчанию
def load_default_config():
    try:
        path_default_config = get_default_config_path()
        with open(path_default_config, "r", encoding="utf-8") as f:
            dict_json_cfg = json.load(f)
    except FileNotFoundError as e:
        print("Default config file not found.\n", e)
        return None
    return dict_json_cfg

# Загружает польз. настройки. если их нет - создает из дефолтных
def load_config():
    user_config_path = get_config_path()
    if os.path.exists(user_config_path):
        with open(user_config_path, "r", encoding="utf-8") as f:
                s_config_dict = json.load(f)
        return s_config_dict
    else:
        load_file_def_cfg = load_default_config()
        save_config(load_file_def_cfg)
        return load_file_def_cfg

# сохраняет переданный словарь в config.json
def save_config(data):
    get_path = get_config_path()
    select_dir = os.path.dirname(get_path)
    if os.path.exists(get_path):
        with open(get_path, "w", encoding="utf-8") as f:
            json.dump(data,f, ensure_ascii=False, indent=4, sort_keys=True)


    else:
        os.makedirs(select_dir, exist_ok=True)
        with open(get_path, "w", encoding="utf-8") as f:
            json.dump(data,f, ensure_ascii=False, indent=4, sort_keys=True)

# def validate_config(data):
#     if isinstance(data, dict):
#         if "source_folder" and "scan_interval_minutes" and "retention_days" and "auto_cleanup" and "rules" and "exceptions" in data:
#             if isinstance(data["source_folder"], str) and isinstance(data["scan_interval_minutes"], int) and isinstance(data["retention_days"], int) and isinstance(data["auto_cleanup"], bool) and isinstance(data["rules"], list) and isinstance(data["exceptions"], list):
#                 if 1 <= data["scan_interval_minutes"] <= 1440 and 1<= data["retention_days"] <= 365:
#                     if os.path.isdir(data["source_folder"]):
#
#                 else:
#                     return False
#
#             else:
#                 return False
#         else:
#             return False
#
#
#     else:
#         return False






