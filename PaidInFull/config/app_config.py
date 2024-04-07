import json


class AppConfig:
    def __init__(self, file_path='config/config.json'):
        self.file_path = file_path
        self.config = self.__load_config()

    def __load_config(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Warning: {self.file_path} not found. Using default values.")
            return {}

    @property
    def FILE_MENU(self):
        return self.config.get('FILE_MENU', 'Plik')

    @property
    def OPEN_CSV_FILE(self):
        return self.config.get('OPEN_CSV_FILE', 'Otwórz zestawienie faktur...')

    @property
    def SETTINGS(self):
        return self.config.get('SETTINGS', 'Ustawienia')

    @property
    def PROCESS_DATA_BUTTON(self):
        return self.config.get('PROCESS_DATA_BUTTON', 'Przetwórz')

    @property
    def ADD_CITY(self):
        return self.config.get('ADD_CITY', 'Dodaj miasto')

    @property
    def ENTER_CITY_NAME(self):
        return self.config.get('ENTER_CITY_NAME', 'Popdaj miasto:')

    @property
    def EDIT_SETTINGS(self):
        return self.config.get('EDIT_SETTINGS', 'Edytuj ustawienia:')

    @property
    def SELLER_INFO_TEXT(self):
        return self.config.get('SELLER_INFO_TEXT', 'Nazwa sprzedawcy:')

    @property
    def CITIES_LIST(self):
        return self.config.get('CITIES_LIST', 'Lista miast (rozdzielona przecinkami):')

    @property
    def APP_NAME(self):
        return self.config.get('APP_NAME', 'PAID IN FULL')

    @property
    def SHOW_SELLER_INFO_BUTTON(self):
        return self.config.get('SHOW_SELLER_INFO_BUTTON', 'Pokaż dane sprzedawcy')

    # Add more properties as needed for other settings SHOW_SELLER_INFO_BUTTON
