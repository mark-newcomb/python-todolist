# Tasklist DB to store every tasklist
import psycopg2

class TasklistDB:
    def __init__(self):
        self.conn = psycopg2.connect(database="postgres",
                            host="localhost",
                            user="marknewcomb",
                            password="196711aa",
                            port="5432")

    def test_db(self):
        cursor = self.conn.cursor()
        cursor.execute("select * from tasklists")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
