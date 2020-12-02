from tkinter import *
from tkinter import ttk


class GUI(object):
    def __init__(self, main_container: Tk):
        self.window = main_container
        self.window.wm_title("Loot Editor v0.98.6")
        self.menu_bar = Menu(self.window)
        self.__create_menu_bar()

    def __create_menu_bar(self):
        # file menus builder
        file_menu = Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Load types.xml...")
        file_menu.add_command(label="Load Trader File...")
        file_menu.add_command(label="Load Database...")
        file_menu.add_separator()
        file_menu.add_command(label="Export types.xml...")
        file_menu.add_command(label="Save Database As...")
        file_menu.add_command(label="(Beta) Export Spawnabletypes...")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.window.destroy)

        # database menus builder
        database_menu = Menu(self.menu_bar, tearoff=0)
        database_menu.add_command(label="Connect...")
        database_menu.add_command(label="Upgrade Database")
        database_menu.add_command(label="Detect Subtypes")
        database_menu.add_separator()
        database_menu.add_command(label="Add items...")
        database_menu.add_command(label="Create item links...")
        database_menu.add_command(label="Trader Editor...")

        # mod menus builder
        mods_menu = Menu(self.menu_bar, tearoff=0)
        mods_menu.add_command(label="Deselect All")
        mods_menu.add_command(label="Select All")
        mods_menu.add_separator()

        # help menus builder
        help_menu = Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label="visit the loot editor github for ")

        # building menu bar
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        self.menu_bar.add_cascade(label="Database", menu=database_menu)
        self.menu_bar.add_cascade(label="Mods In Use", menu=mods_menu)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)

        # configuring menu bar
        self.window.config(menu=self.menu_bar)


window = Tk()
GUI(window)
window.mainloop()
