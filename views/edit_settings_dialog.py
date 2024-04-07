import tkinter as tk
from tkinter import simpledialog, scrolledtext

from config.app_config import AppConfig


class EditSettingsDialog(simpledialog.Dialog):
    def __init__(self, parent, title, initial_seller_info, initial_cities_list):
        # convert tabs or new lines if necessary
        self.__app_config = AppConfig()
        self.updated_cities_list = None
        self.updated_seller_info = None
        self.__cities_list_text_area = None
        self.__seller_info_text_entry = None
        self.__initial_seller_info = initial_seller_info.replace("\n", "\n").replace("\t", "\t")
        self.__initial_cities_list = initial_cities_list
        super().__init__(parent, title)

    def body(self, parent):
        tk.Label(parent, text=self.__app_config.SELLER_INFO_TEXT).grid(row=0, column=0, sticky="w")
        self.__seller_info_text_entry = scrolledtext.ScrolledText(parent, width=50, height=10)
        self.__seller_info_text_entry.focus_set()
        self.__seller_info_text_entry.grid(row=1, column=0, sticky="ew")
        self.__seller_info_text_entry.insert(tk.END, self.__initial_seller_info)
        self.__seller_info_text_entry.bind('<Return>', self.__on_enter_pressed)

        tk.Label(parent, text=self.__app_config.CITIES_LIST).grid(row=2, column=0, sticky="nw")
        self.__cities_list_text_area = scrolledtext.ScrolledText(parent, height=10, width=50)
        self.__cities_list_text_area.grid(row=3, column=0, sticky="ew")
        self.__cities_list_text_area.insert(tk.END, ', '.join(self.__initial_cities_list))

        return self.__seller_info_text_entry  # initial focus

    def apply(self):
        # reconvert new lines and tabs if necessary
        self.updated_seller_info = (self.__seller_info_text_entry
                                    .get("1.0", tk.END).strip()
                                    .replace("\n", "\n")
                                    .replace("\t", "\t"))
        cities_text = self.__cities_list_text_area.get("1.0", tk.END).strip()
        self.updated_cities_list = [city.strip() for city in cities_text.split(',') if city.strip()]

    def __on_enter_pressed(self, _event):
        """Insert a newline in the ScrolledText widget when Enter is pressed."""
        self.__seller_info_text_entry.insert(tk.INSERT, "\n")
        return "break"  # Prevent the event from propagating to the dialog
