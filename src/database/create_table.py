from src.database.database import config
import psycopg2


def create_tables():
    """ create tables in the PostgreSQL database"""
    sql = '''CREATE TABLE VISITORS(
       ID SERIAL UNIQUE NOT NULL,
       NUM_POOL_VISITORS INTEGER,
       NUM_SAUNA_VISITORS INTEGER,
       DATE TIMESTAMP WITH TIME ZONE
    )'''
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        cur.execute(sql)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__.py':
    create_tables()
