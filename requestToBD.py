import sqlite3

db = sqlite3.connect("load.db")
sql = db.cursor()

def download_streets():
    with open("streetsBlag.txt", "r", encoding="utf-8") as file:
        s_id = 1
        while (street := file.readline().replace("\n", "")) != "":
            sqlite_insert_query = "INSERT INTO roads (road_id, name) VALUES (?, ?);"
            data = (s_id, street)
            sql.execute(sqlite_insert_query, data)
            db.commit()
            s_id += 1
