from psycopg2 import pool
import quiet.long as f


connection_pool = pool.SimpleConnectionPool(1,
                                            1,
                                            user="postgres",
                                            password=f.pasw,
                                            database="learning",
                                            host="localhost")

# def connect():
#     return psycopg2.connect(
#             user="postgres",
#             password=f.pasw,
#             database="learning",
#             host="localhost"
#             )

class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self): # Called at the beginning of the With statement
        self.connection = connection_pool.getconn()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_val, exception_tb): # All exception values, fails, errors
        if exception_val is not None: #eg TypeError, ValueError
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        connection_pool.putconn(self.connection)