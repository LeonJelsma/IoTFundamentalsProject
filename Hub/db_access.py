import os
import sqlite3
from sqlite3 import Error
import const


def init_database():
    if not os.path.exists(const.DB_DIR):
        os.makedirs(const.DB_DIR)
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS "Measurements" (
            "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "deviceId"	INTEGER NOT NULL,
            "humidity"	TEXT NOT NULL,
            "temperature"   TEXT NOT NULL,
            "pressure"  TEXT NOT NULL,
            "timestamp" TEXT NOT NULL
            );''')
    conn.close()


def create_connection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(const.DB_FILE)
    except Error as e:
        print(e)
    return conn


def get_measurements(conn):
    sql = '''SELECT * FROM Measurements'''
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    measurements = []
    index = 0
    if len(result) < 1:
        return result
    else:
        for entry in result:
            measurements.append({
                "id": entry[0],
                "deviceId": entry[1],
                "humidity": entry[2],
                "pressure": entry[3],
                "temperature": entry[4],
                "timestamp": entry[5]
            })
    return measurements


def add_measurement(conn, measurement):
    sql = '''INSERT INTO Measurements(deviceId, humidity, temperature, pressure, timestamp) VALUES(?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, (
        measurement["deviceId"],
        measurement["humidity"],
        measurement["temperature"],
        measurement["pressure"],
        measurement["timestamp"]
    ))
    conn.commit()


def delete_measurement(conn, id):
    sql = '''DELETE FROM Measurements WHERE id like ?'''
    cur = conn.cursor()
    cur.execute(sql, [str(id)])
    conn.commit()


def failed_measurements_exist(conn):
    sql = '''SELECT * FROM Measurements'''
    cur = conn.cursor()
    cur.execute(sql)
    return len(cur.fetchall()) > 0
