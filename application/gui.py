from tkinter import *
from tkinter import ttk
from application import Config
from application import Database
from application import Item
from application.autocompleteCombobox import Combobox_Autocomplete


class GUI(object):
    def __init__(self, main_container: Tk):
        #
        self.config = Config('config.xml')
        self.database = Database("test_scripts/test_db/test_3.db")
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
        self.__create_side_bar()
        self.__populate_items()
        #
        self.tree.bind("<ButtonRelease-1>", self.__fill_entry_frame)

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
        self.id = IntVar()
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

        Button(self.checkBoxFrame, text="Update", width=8, command=self.__update_item). \
            grid(row=5, column=0, pady=5, sticky="w")

        Button(self.checkBoxFrame, text="Delete", width=8, command=self.__delete_item). \
            grid(row=5, column=1, pady=5, sticky="w")

    def __create_tree_view(self):
        self.treeFrame = Frame(self.window)
        self.treeFrame.grid(row=0, column=1, sticky="nsew")

        self.treeFrame.grid_rowconfigure(0, weight=1)
        self.treeFrame.grid_columnconfigure(0, weight=1)
        self.column_info = self.config.get_tree_heading()
        self.tree = ttk.Treeview(self.treeFrame, columns=self.column_info[0], height=40)
        for col in self.column_info[1]:
            self.tree.heading(col[2], text=col[0], command=lambda _col=col[0]:
            self.treeview_sort_column(self.tree, _col, False), )
            self.tree.column(col[2], width=col[1], stretch=0)

        self.tree.grid(row=0, column=0, sticky="nsew")
        self.treeView = self.tree

        vertical = ttk.Scrollbar(self.treeFrame, orient=VERTICAL)
        horizontal = ttk.Scrollbar(self.treeFrame, orient=HORIZONTAL)

        vertical.grid(row=0, column=1, sticky="ns")
        horizontal.grid(row=1, column=0, sticky="we")
        self.tree.config(yscrollcommand=vertical.set)
        self.tree.config(xscrollcommand=horizontal.set)
        vertical.config(command=self.tree.yview)
        horizontal.config(command=self.tree.xview)

    def __create_side_bar(self):
        self.filterFrameHolder = Frame(self.window)
        self.filterFrameHolder.grid(row=0, column=2, sticky="n")

        self.filterFrame = LabelFrame(self.filterFrameHolder, text="Filter")
        self.filterFrame.grid(row=1, column=0, pady=5)

        Label(self.filterFrame, text="Type").grid(row=1, column=0, sticky="w")
        Label(self.filterFrame, text="Subtype").grid(row=2, column=0, sticky="w")

        self.type_for_filter = StringVar()
        self.type_for_filter.set("all")
        OptionMenu(self.filterFrame, self.type_for_filter, *self.config.get_types()). \
            grid(row=1, column=1, sticky="w", padx=5)
        self.sub_type_combo_for_filter = Combobox_Autocomplete(self.filterFrame, self.config.get_sub_types(),
                                                               highlightthickness=1, width=15)
        self.sub_type_combo_for_filter.grid(row=2, column=1, sticky="w", pady=5, padx=5)

        Button(self.filterFrame, text="Filter", width=12, command=self.__filter_items).grid(columnspan=2, pady=5,
                                                                                            padx=10, sticky='nesw')

    def __update_item(self):
        updated_item = Item()
        updated_item.id = self.id.get()
        updated_item.name = self.name.get()
        updated_item.nominal = self.nominal.get()
        self.database.update_item(updated_item)
        self.__populate_items()

    def __delete_item(self):
        self.database.delete_item(self.id.get())
        self.__populate_items()

    def __populate_items(self, items=None):
        if items is None:
            items = self.database.all_items()
        if self.tree.get_children() != ():
            self.tree.delete(*self.tree.get_children())
        for i in items:
            self.tree.insert("", "end", text=i[0], value=i[1:13])

    def __filter_items(self):
        item_type = self.type_for_filter.get()
        if item_type == "all":
            self.__populate_items(self.database.all_items())
        else:
            if self.sub_type_combo_for_filter.get() != "":
                sub_type = self.sub_type_combo_for_filter.get()
            else:
                sub_type = None
            self.__populate_items(self.database.filter_items(item_type, sub_type))
        self.name.set("Test")
        print(item_type)

    def __fill_entry_frame(self, event):
        tree_row = self.tree.item(self.tree.focus())
        id = tree_row['text']
        item = self.database.get_item(id)
        self.id.set(id)
        self.name.set(item.name)
        self.nominal.set(item.nominal)
        self.min.set(item.min)
        self.lifetime.set(item.lifetime)
        self.restock.set(item.restock)
        self.mod.set(item.mod)
        self.trader.set(item.trader)
        self.dynamic_event.set(item.dynamic_event)
        self.count_in_hoarder.set(item.count_in_hoarder)
        self.count_in_cargo.set(item.count_in_cargo)
        self.count_in_map.set(item.count_in_map)
        self.count_in_player.set(item.count_in_player)


window = Tk()
GUI(window)
window.mainloop()
