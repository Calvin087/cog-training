import psycopg2
import quiet.long as f

def connect():
    return psycopg2.connect(
            user="postgres",
            password=f.pasw,
            database="learning",
            host="localhost"
            )