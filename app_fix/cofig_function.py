import psycopg2

def get_connetion ():
    conn = psycopg2.connect(    
        host = 'localhost',
        database = 'test',
        user = 'postgres',
        password = '12345',
        port = '5432'
        )
    
    return conn