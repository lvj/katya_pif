import tkinter as tk
from tkinter import ttk, messagebox
from config.app_config import AppConfig


class View:
    def __init__(self, master):
        self.app_config = AppConfig()
        self.process_data_button = None
        self.cities_combobox = None
        self.master = master
        self.__show_info_btn = None
        self.__file_menu = None
        self.__menubar = None
        self.file_path_label = None
        self.__configure_window()
        self.__create_widgets()

    def __configure_window(self):
        self.master.iconbitmap(r'_resources/images/ico.ico')
        self.master.geometry('800x600+100+100')

    def __create_widgets(self):
        self.__menubar = tk.Menu(self.master)
        self.__file_menu = tk.Menu(self.__menubar, tearoff=0)
        self.__file_menu.add_command(label=self.app_config.OPEN_CSV_FILE)
        self.__file_menu.add_command(label=self.app_config.SETTINGS)
        self.__menubar.add_cascade(label=self.app_config.FILE_MENU, menu=self.__file_menu)

        self.process_data_button = ttk.Button(self.master, text=self.app_config.PROCESS_DATA_BUTTON, width=30)
        self.process_data_button.grid(row=0, column=0, sticky="w")
        # self.process_data_button.pack()

        self.master.config(menu=self.__menubar)
        # Seller Info Button
        self.__show_info_btn = ttk.Button(self.master, text=self.app_config.SHOW_SELLER_INFO_BUTTON, width=30)
        self.__show_info_btn.grid(row=1, column=0, sticky="w")
        # self.__show_info_btn.pack()

        # Cities Combobox
        self.cities_combobox = ttk.Combobox(self.master, width=30)
        self.cities_combobox.grid(row=0, column=1, sticky="w")
        # self.cities_combobox.pack()
        self.file_path_label = ttk.Label(text="pusty")
        self.file_path_label.grid(row=2, column=0, sticky="w")

    def set_cities_list(self, cities):
        self.cities_combobox['values'] = cities

    def set_file_path_label(self, path):
        self.file_path_label['text'] = path

    def set_info_button_command(self, command):
        self.__show_info_btn.config(command=command)

    def set_menu_command(self, menu_label, command):
        if menu_label == self.app_config.OPEN_CSV_FILE:
            self.__file_menu.entryconfig(self.app_config.OPEN_CSV_FILE, command=command)
        elif menu_label == self.app_config.SETTINGS:
            self.__file_menu.entryconfig(self.app_config.SETTINGS, command=command)

    def show_message(self, info):
        messagebox.showinfo(self.app_config.SELLER_INFO_TEXT, info)
