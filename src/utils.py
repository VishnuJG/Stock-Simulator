import psycopg2

def connect_db(user, password):
    try:
        connection = psycopg2.connect(user=user, password=password, host='127.0.0.1', port='5432', database='stocksdb2')
        return connection
    except Exception as e:
        print('Database connection error:', e)
        return None

# Additional utility functions for database operations