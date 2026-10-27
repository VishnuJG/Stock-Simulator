import psycopg2

class Database:
    def __init__(self, user, password, host='127.0.0.1', port='5432', database='stocksdb2'):
        self.connection = psycopg2.connect(user=user, password=password, host=host, port=port, database=database)
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetch_all(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()