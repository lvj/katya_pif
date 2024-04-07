import json
import os


class Model:
    def __init__(self, settings_file=r"settings.json"):
        self.__settings_file = settings_file
        self.settings = self.__load_settings()

    def __load_settings(self):
        if not os.path.exists(self.__settings_file):
            return {}

        encodings = ['utf-8']
        for encoding in encodings:
            try:
                with open(self.__settings_file, 'r', encoding=encoding) as file:
                    return json.load(file)
            except UnicodeDecodeError:
                pass  # try next

        # none matched, raise error
        raise ValueError(f"Failed to load {self.__settings_file} - incompatible encoding.")

    def save_settings(self, settings):
        with open(self.__settings_file, "w", encoding='utf-8') as file:
            json.dump(settings, file, ensure_ascii=False, indent=4)
        self.settings = settings

    def get_seller_info(self):
        return self.settings['seller_info_text']

    def get_cities_list(self):
        return self.settings['cities_list']
