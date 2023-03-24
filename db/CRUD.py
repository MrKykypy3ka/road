import sqlite3

db = sqlite3.connect('db/load.db')
sql = db.cursor()


def save_time(self):
    self.uil.timeList.addItem(self.uil.timeEdit.text())
    try:
        time_id = 1
        for elem in [self.uia.timeList.item(i).text() for i in range(self.uia.crossroadList.count())]:
            time = elem
            sqlite_insert_query = """INSERT INTO times (time_id, time) VALUES (?, ?);"""
            data = (time_id, time)
            self.sql.execute(sqlite_insert_query, data)
            self.db.commit()
            time_id += 1
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        print("Данные успешно загружены!")


def save_bad_sections(self):
    try:
        badSection_id = 1
        for elem in [self.uia.badRoadList.item(i).text() for i in range(self.uia.badRoadList.count())]:
            temp = elem.replace(',', '').replace('(', '').replace(')', '').split()
            longitude = temp[0]
            latitude = temp[1]

            sqlite_insert_query = """INSERT INTO badSections (badSection_id, street,
             longitude, latitude, count_lane, max_speed) VALUES (?, ?, ?, ?, ?, ?);"""
            data = (badSection_id, "", longitude, latitude, 0, 0)
            self.sql.execute(sqlite_insert_query, data)
            self.db.commit()
            badSection_id += 1
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        print("Данные успешно загружены!")

def save_road(self):
    try:
        road_id = 1
        for elem in [self.uia.roadList.item(i).text() for i in range(self.uia.roadList.count())]:
            temp = elem.replace(',', '').replace('(', '').replace(')', '').split()
            longitude = temp[0]
            latitude = temp[1]

            sqlite_insert_query = """INSERT INTO roads (road_id, street,
             longitude, latitude, count_lanes, max_speed) VALUES (?, ?, ?, ?, ?, ?);"""
            data = (road_id, "", longitude, latitude, 0, 0)
            self.sql.execute(sqlite_insert_query, data)
            self.db.commit()
            road_id += 1
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        print("Данные успешно загружены!")

def save_crossroad(self):
    try:
        crossroad_id = 1
        for elem in [self.uia.crossroadList.item(i).text() for i in range(self.uia.crossroadList.count())]:
            temp = elem.replace(',', '').replace('(', '').replace(')', '').split()
            longitude = temp[0]
            latitude = temp[1]
            sqlite_insert_query = """INSERT INTO crossroads (crossroad_id, street,
             longitude, latitude, trafficLights) VALUES (?, ?, ?, ?, ?);"""
            data = (crossroad_id, "", longitude, latitude, 0)
            self.sql.execute(sqlite_insert_query, data)
            self.db.commit()
            crossroad_id += 1
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        print("Данные успешно загружены!")
