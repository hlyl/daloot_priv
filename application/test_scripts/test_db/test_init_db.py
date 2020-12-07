import sqlite3

from application import InitDatabase

DATABASE = "test.db"


def test_init_database():
    database = InitDatabase(DATABASE)
    database.create_table()

    db_connection = sqlite3.connect(database.db_name)
    db_cursor = db_connection.cursor()
    items = db_cursor.execute("pragma table_info('items')").fetchall()
    db_connection.commit()
    db_connection.close()
    print(items)
    assert items == [(0, 'id', 'INTEGER', 0, None, 1), (1, 'name', 'VARCHAR(30)', 0, None, 0),
                     (2, 'nominal', 'INTEGER', 0, None, 0), (3, 'mean', 'INTEGER', 0, None, 0),
                     (4, 'restock', 'INTEGER', 0, None, 0), (5, 'life_time', 'INTEGER', 0, None, 0),
                     (6, 'usage', 'VARCHAR(30)', 0, None, 0), (7, 'tire', 'VARCHAR(30)', 0, None, 0),
                     (8, 'rarity', 'VARCHAR(30)', 0, None, 0), (9, 'gun_type', 'VARCHAR(30)', 0, None, 0),
                     (10, 'sub_type', 'VARCHAR(30)', 0, None, 0), (11, 'mod', 'VARCHAR(30)', 0, None, 0),
                     (12, 'trader', 'INTEGER', 0, None, 0), (13, 'dynamic_event', 'INTEGER', 0, None, 0),
                     (14, 'count_in_cargo', 'INTEGER', 0, None, 0), (15, 'count_in_hoarder', 'INTEGER', 0, None, 0),
                     (16, 'count_in_map', 'INTEGER', 0, None, 0), (17, 'count_in_player', 'INTEGER', 0, None, 0)]
