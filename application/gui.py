from tkinter import *
from tkinter import ttk
from application import Config

from application.autocompleteCombobox import Combobox_Autocomplete


class GUI(object):
    def __init__(self, main_container: Tk):
        #
        self.config = Config('config.xml')
        #
        self.window = main_container
        self.window.wm_title("Loot Editor v0.98.6")
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.menu_bar = Menu(self.window)
        #
        self.__create_menu_bar()
        self.__create_entry_frame()
        self.__create_tree_view()

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

    def __create_entry_frame(self):
        self.entryFrameHolder = Frame(self.window)
        self.entryFrameHolder.grid(row=0, column=0, sticky="nw")
        self.entryFrame = Frame(self.entryFrameHolder)
        self.entryFrame.grid(padx=8, pady=6)
        # labels
        Label(self.entryFrame, text="Name").grid(row=0, column=0, sticky="w", pady=5)
        Label(self.entryFrame, text="Nominal").grid(row=1, column=0, sticky="w", pady=5)
        Label(self.entryFrame, text="Min").grid(row=2, column=0, sticky="w", pady=5)
        Label(self.entryFrame, text="Restock").grid(row=3, column=0, sticky="w", pady=5)
        Label(self.entryFrame, text="Lifetime").grid(row=4, column=0, sticky="w", pady=5)
        Label(self.entryFrame, text="Usages").grid(row=5, column=0, sticky="w", pady=5)
        Label(self.entryFrame, text="Tiers").grid(row=6, column=0, sticky="w", pady=5)
        Label(self.entryFrame, text="Type").grid(row=7, column=0, sticky="w", pady=5)
        Label(self.entryFrame, text="Sub Type").grid(row=8, column=0, sticky="w", pady=5)
        Label(self.entryFrame, text="Rarity").grid(row=9, column=0, sticky="w", pady=5)
        Label(self.entryFrame, text="Mod").grid(row=10, column=0, sticky="w", pady=5)
        Label(self.entryFrame, text="Trader").grid(row=11, column=0, sticky="w", pady=5)
        # input variables
        self.name = StringVar()
        self.nominal = StringVar()
        self.min = StringVar()
        self.restock = StringVar()
        self.lifetime = StringVar()
        self.usages = StringVar()
        self.tires = StringVar()
        self.type = StringVar()
        self.sub_type = StringVar()
        self.rarity = StringVar()
        self.mod = StringVar()
        self.trader = StringVar()
        self.dynamic_event = IntVar()
        self.count_in_cargo = IntVar()
        self.count_in_hoarder = IntVar()
        self.count_in_map = IntVar()
        self.count_in_player = IntVar()
        # form fields
        self.nameField = Entry(self.entryFrame, textvariable=self.name)
        self.nameField.grid(row=0, column=1, sticky="w")
        self.nominalField = Entry(self.entryFrame, textvariable=self.nominal)
        self.nominalField.grid(row=1, column=1, sticky="w")
        self.minField = Entry(self.entryFrame, textvariable=self.min)
        self.minField.grid(row=2, column=1, sticky="w")
        self.restockField = Entry(self.entryFrame, textvariable=self.restock)
        self.restockField.grid(row=3, column=1, sticky="w")
        self.lifetimeField = Entry(self.entryFrame, textvariable=self.lifetime)
        self.lifetimeField.grid(row=4, column=1, sticky="w")
        self.usagesListBox = Listbox(self.entryFrame, height=4, selectmode="multiple", exportselection=False, )
        self.usagesListBox.grid(row=5, column=1, pady=5, sticky="w")
        self.tiersListBox = Listbox(self.entryFrame, height=4, selectmode="multiple", exportselection=False, )
        self.tiersListBox.grid(row=6, column=1, pady=5, sticky="w")
        self.typeOption = OptionMenu(self.entryFrame, self.type, ('Type1', 'Type2'))
        self.typeOption.grid(row=7, column=1, sticky="w", pady=5)
        self.subtypeAutoComp = Combobox_Autocomplete(self.entryFrame, ["test", "yes"], highlightthickness=1)
        self.subtypeAutoComp.grid(row=8, column=1, sticky="w", pady=5)
        self.rarityOption = OptionMenu(self.entryFrame, self.rarity, ["Rarity"])
        self.rarityOption.grid(row=9, column=1, sticky="w", pady=5)
        self.modField = Entry(self.entryFrame, textvariable=self.mod)
        self.modField.grid(row=10, column=1, sticky="w", pady=5)
        self.traderField = Entry(self.entryFrame, textvariable=self.trader)
        self.traderField.grid(row=11, column=1, sticky="w")
        # check boxes frame
        self.checkBoxFrame = Frame(self.entryFrameHolder)
        self.checkBoxFrame.grid(row=1, column=0, columnspan=2, sticky="w")
        self.dynamic_event_check = Checkbutton(self.checkBoxFrame, text="Dynamic Event", variable=self.dynamic_event)
        self.dynamic_event_check.grid(row=0, column=0, sticky="w")
        self.count_in_cargo_check = Checkbutton(self.checkBoxFrame, text="Count in Cargo", variable=self.count_in_cargo)
        self.count_in_cargo_check.grid(row=1, column=0, sticky="w")
        self.count_in_hoarder_check = Checkbutton(self.checkBoxFrame, text="Count in Hoarder",
                                                  variable=self.count_in_hoarder)
        self.count_in_hoarder_check.grid(row=2, column=0, sticky="w")
        self.count_in_map_check = Checkbutton(self.checkBoxFrame, text="Count in Map", variable=self.count_in_map)
        self.count_in_map_check.grid(row=3, column=0, sticky="w")
        self.count_in_player_check = Checkbutton(self.checkBoxFrame, text="Count in Player",
                                                 variable=self.count_in_player)
        self.count_in_player_check.grid(row=4, column=0, sticky="w")

        Button(self.checkBoxFrame, text="Update", width=8, command=self.update_item()). \
            grid(row=5, column=0, pady=5, sticky="w")

        Button(self.checkBoxFrame, text="Delete", width=8, command=self.delete_item()). \
            grid(row=5, column=1, pady=5, sticky="w")

    def __create_tree_view(self):
        self.treeFrame = Frame(self.window)
        self.treeFrame.grid(row=0, column=1, sticky="nsew")
        self.treeFrame.grid_rowconfigure(0, weight=1)
        self.treeFrame.grid_columnconfigure(0, weight=1)
        self
        columns = (
            "nominal",
            "min",
            "restock",
            "lifetime",
            "type",
            "subtype",
            "usage",
            "tier",
            "Dyn. Event",
            "rarity",
            "mod",
            "trader",
        )
        self.tree = ttk.Treeview(self.treeFrame, columns=columns, height=40)
        for col in columns:
            self.tree.heading(
                col,
                text=col,
                command=lambda _col=col: self.treeview_sort_column(
                    self.tree, _col, False
                ),
            )

        self.tree.grid(row=0, column=0, sticky="nsew")
        self.treeview = self.tree

        vert = ttk.Scrollbar(self.treeFrame, orient=VERTICAL)
        hori = ttk.Scrollbar(self.treeFrame, orient=HORIZONTAL)

        vert.grid(row=0, column=1, sticky="ns")
        hori.grid(row=1, column=0, sticky="we")
        self.tree.config(yscrollcommand=vert.set)
        self.tree.config(xscrollcommand=hori.set)
        vert.config(command=self.tree.yview)
        hori.config(command=self.tree.xview)

    def update_item(self):
        pass

    def delete_item(self):
        pass


window = Tk()
GUI(window)
window.mainloop()
