import sqlite3


class InitDatabase(object):
    def __init__(self, db_name):
        self.db_name = db_name
        self.sql_create_usages_table = """CREATE TABLE IF NOT EXISTS usages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usage VARCHAR(30) NOT NULL);"""
        self.sql_create_tires_table = """CREATE TABLE IF NOT EXISTS tires (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tire VARCHAR(30) NOT NULL);"""
        self.sql_create_rarities_table = """CREATE TABLE IF NOT EXISTS rarities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                rarity VARCHAR(30) NOT NULL);"""
        self.sql_create_types_table = """CREATE TABLE IF NOT EXISTS types (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                gun_type VARCHAR(30) NOT NULL);"""
        self.sql_create_sub_types_table = """CREATE TABLE IF NOT EXISTS sub_types (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                gun_type INTEGER NOT NULL,
                sub_type VARCHAR(30) NOT NULL,
                FOREIGN KEY (gun_type) REFERENCES types(id));"""
        self.sql_create_items_table = """CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(30) NOT NULL,
                nominal INTEGER NOT NULL,
                mean INTEGER NOT NULL,
                restock INTEGER NOT NULL,
                life_time INTEGER NOT NULL,
                usage INTEGER NOT NULL,
                tire INTEGER NOT NULL,
                rarity INTEGER NOT NULL,
                gun_type INTEGER NOT NULL,
                sub_type INTEGER NOT NULL,
                mod VARCHAR(30) NOT NULL,
                trader INTEGER NOT NULL,
                dynamic_event INTEGER NOT NULL,
                count_in_cargo INTEGER NOT NULL,
                count_in_hoarder INTEGER NOT NULL,
                count_in_map INTEGER NOT NULL,
                count_in_player INTEGER NOT NULL,
                FOREIGN KEY (usage) REFERENCES usages(id),
                FOREIGN KEY (tire) REFERENCES tires(id),
                FOREIGN KEY (rarity) REFERENCES rarities(id),
                FOREIGN KEY (gun_type) REFERENCES types(id),
                FOREIGN KEY (sub_type) REFERENCES sub_types(id));
                """

    def create_tables(self):
        # database connection
        db_connection = sqlite3.connect(self.db_name)
        # cursor
        db_cursor = db_connection.cursor()
        # executing sql statements for creating tables specified above
        db_cursor.execute(self.sql_create_usages_table)
        db_cursor.execute(self.sql_create_tires_table)
        db_cursor.execute(self.sql_create_rarities_table)
        db_cursor.execute(self.sql_create_types_table)
        db_cursor.execute(self.sql_create_sub_types_table)
        db_cursor.execute(self.sql_create_items_table)
        # committing changes to the database
        db_connection.commit()
        # closing database connection
        db_connection.close()
