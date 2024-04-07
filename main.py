import tkinter as tk
from controllers.controller import Controller
from config.app_config import AppConfig

# todo
app_config = AppConfig()


if __name__ == "__main__":
    root = tk.Tk()
    root.title(app_config.APP_NAME)

    app = Controller(root)
    root.mainloop()
