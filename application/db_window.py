from tkinter import *

from application import InitDatabase
import windows


class DBWindow(object):
    DATABASE_NAME = "dayz_items"
    INI_FILE = "app.ini"

    def __init__(self, root):
        self.window = Toplevel(root)
        self.window.grab_set()

        self.configFrame = Frame(self.window)
        self.configFrame.grid(row=1, column=0, sticky="n,w,e", padx=30)
        db_actions = [("New Database", "new"), ("Use Existing", "existing")]
        self.selected_db_action = StringVar()
        self.selected_db_action.set("existing")

        Radiobutton(self.configFrame, text=db_actions[0][0], variable=self.selected_db_action,
                    value=db_actions[0][1]).grid(row=6, column=0,
                                                 pady=10)
        Radiobutton(self.configFrame, text=db_actions[1][0], variable=self.selected_db_action,
                    value=db_actions[1][1]).grid(row=6, column=1)

        Label(self.configFrame, text="Database Name").grid(row=7, column=0, sticky="w")

        self.db_name = StringVar()
        self.db_name.set(self.DATABASE_NAME)
        self.db_name_entry = Entry(self.configFrame, textvariable=self.db_name)
        self.db_name_entry.grid(row=7, column=1, sticky="e", pady=5)

        button_frame = Frame(self.window)
        button_frame.grid(row=2, column=0, columnspan=3, pady=10)
        Button(button_frame, text="Init Database", width=12, command=self.__init_db).grid(row=0, column=1, sticky="w",
                                                                                          padx=5)
        # windows.center(self.window)
        self.window.wait_window()

    def __init_db(self):
        if self.selected_db_action.get() == "new":
            InitDatabase(self.db_name.get() + ".db")
            print("New Database")

    '''def openTypes(self):
        self.typesDir.set(windows.openFile("xml"))

    def createTest(self):
        if self.v.get() == "create":
            self.passParams()
            self.createDatabase()
            windows.connectionSuccess(self.window)
            if self.typesDir.get() != "":
                windows.writeTypesToDatabase(self.typesDir.get())
        else:
            self.testDB()

    def createDatabase(self):
        try:
            dao.createDB(self.database.get())
            dao.loadDB(windows.getContent(windows.dataPath + "\\GENESIS.sql"))
        except Exception as e:
            windows.showError(self.window, "Error", "Failed to connect:\n" + str(e))
            windows.deleteParams()

    def testDB(self):
        self.passParams()
        try:
            dao.getNominalByType("gun")
            windows.connectionSuccess(self.window)
        except Exception as e:
            windows.showError(self.window, "Error", "Failed to connect:\n" + str(e))
            windows.deleteParams()

    def set(self):
        self.passParams()
        self.window.destroy()
        dao.setColumnNames()

    def passParams(self):
        dao.setConnectionParams(self.username.get(),
                                self.password.get(),
                                self.port.get(),
                                self.database.get(),
                                self.HostName.get(),
                                "8.0")

        dao.setConnectionParams(self.username.get(),
                                self.password.get(),
                                self.port.get(),
                                self.database.get(),
                                self.HostName.get(),
                                dao.getOdbcVersion())'''


def testWindow():
    window = Tk()
    DBWindow(window)

    window.mainloop()
