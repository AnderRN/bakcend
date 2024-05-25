import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='dbapis'
        )
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        self.conn.commit()
        return self.cursor

    def fetch_all(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetch_one(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()
