import sqlite3


conn = sqlite3.connect('gulfstream_database.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Aircraft (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Performance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aircraft_id INTEGER NOT NULL,
        maximum_range REAL,
        high_speed_cruise REAL,
        long_range_cruise REAL,
        FOREIGN KEY (aircraft_id) REFERENCES Aircraft (id)
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Cabin (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aircraft_id INTEGER NOT NULL,
        living_areas INTEGER,
        num_panoramic_windows INTEGER,
        total_interior_length REAL,
        FOREIGN KEY (aircraft_id) REFERENCES Aircraft (id)
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Systems (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aircraft_id INTEGER NOT NULL,
        avionics TEXT,
        engines TEXT,
        FOREIGN KEY (aircraft_id) REFERENCES Aircraft (id)
    )
''')


conn.commit()
conn.close()
