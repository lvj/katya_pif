from tkinter import filedialog, messagebox
from models.model import Model
from views.view import View
from views.edit_settings_dialog import EditSettingsDialog
from config.app_config import AppConfig


class Controller:
    def __init__(self, master):
        self.master = master
        self.model = Model()
        self.view = View(master)
        self.__app_config = AppConfig()
        self.__bind_commands()

    def __bind_commands(self):
        # get cities from das model
        self.view.set_cities_list(self.model.get_cities_list())
        # bind commands
        self.view.set_info_button_command(self.__show_seller_info)
        self.view.set_menu_command(self.__app_config.OPEN_CSV_FILE, command=self.__open_csv_file)
        self.view.set_menu_command(self.__app_config.SETTINGS, command=self.__edit_settings)
        self.view.process_data_button.config(command=self.__process_data)
        self.view.cities_combobox.bind("<<ComboboxSelected>>", self.__on_city_selected)

    def __show_seller_info(self):
        info = self.model.get_seller_info()
        self.view.show_message(info)
        # self.view.show_message(info.replace('<br/>', '\n'))

    @staticmethod
    def __open_csv_file():
        file_path = filedialog.askopenfilename(filetypes=[("Pliki CSV", "*.csv")])
        if file_path:
            messagebox.showinfo("Info", f"Wybrany plik: {file_path}")

    def __edit_settings(self):
        current_seller_info = self.model.get_seller_info()
        current_cities_list = self.model.get_cities_list()
        dialog = EditSettingsDialog(self.view.master, self.__app_config.EDIT_SETTINGS, current_seller_info,
                                    current_cities_list)

        if hasattr(dialog, 'updated_seller_info') and hasattr(dialog, 'updated_cities_list'):
            self.model.settings['seller_info_text'] = dialog.updated_seller_info
            self.model.settings['cities_list'] = dialog.updated_cities_list
            self.model.save_settings(self.model.settings)
            # refresh?
        self.view.cities_combobox['values'] = self.model.settings['cities_list']

    @staticmethod
    def __process_data():
        messagebox.showinfo("Info", "Hello world")

    def __on_city_selected(self, _event):
        # Get the selected city
        selected_city = self.view.cities_combobox.get()
        # Display a message
        messagebox.showinfo("Wybrane miasto", f"Wybrałeś: {selected_city}")
