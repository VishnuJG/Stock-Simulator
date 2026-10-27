import psycopg2

class Database:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(user=self.user, password=self.password, host='127.0.0.1', port='5432', database='stocksdb2')
        except Exception as e:
            print('Database connection error:', e)

    def close(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query):
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()