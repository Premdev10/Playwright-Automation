import configparser
import os

class ConfigReader:
    @staticmethod
    def get_config_value(section, key):
        config = configparser.ConfigParser()
        config_path = os.path.join(os.path.dirname(__file__), '../config/config.ini')
        config.read(config_path)
        return config.get(section, key)
