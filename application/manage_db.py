import sqlite3
from application import Item


class Database(object):
    def __init__(self, db_name):
        self.db_name = db_name

    '''
    CRUD Operations related to usages
    '''

    def create_usage(self, usage):
        # database connection
        db_connection = sqlite3.connect(self.db_name)
        # sql statement
        sql_create_usage = "INSERT INTO usages(usage) VALUES(?)"
        # database cursor
        db_cursor = db_connection.cursor()
        db_cursor.execute(sql_create_usage, (usage,))
        db_connection.commit()
        db_connection.close()

    def update_usage(self, usage_id, usage):
        pass

    def delete_usage(self, usage_id):
        pass

    def all_usages(self):
        pass
