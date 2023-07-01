import sqlite3
from models import *
from typing import Optional


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('gulfstream_database.db', check_same_thread=False)
        self.cursor = self.conn.cursor()

    # Aircraft
    def create_aircraft(self, aircraft: Aircraft):
        self.cursor.execute("INSERT INTO Aircraft (name) VALUES (?)", (aircraft.name,))
        self.conn.commit()

    def get_air_crafts(self):
        self.cursor.execute("SELECT * FROM Aircraft")
        aircraft = self.cursor.fetchall()
        return aircraft

    def get_aircraft(self, aircraft_id: int):
        self.cursor.execute("SELECT * FROM Aircraft WHERE id = ?", (aircraft_id,))
        aircraft = self.cursor.fetchone()
        return aircraft

    def update_aircraft(self, aircraft_id: int, aircraft: Aircraft):
        self.cursor.execute("UPDATE Aircraft SET name = ? WHERE id = ?", (aircraft.name, aircraft_id))
        self.conn.commit()

    def delete_aircraft(self, aircraft_id: int):
        self.cursor.execute("DELETE FROM Aircraft WHERE id = ?", (aircraft_id,))
        self.conn.commit()

    # Performance
    def create_performance(self, performance: Performance):
        self.cursor.execute(
            "INSERT INTO Performance (aircraft_id, maximum_range, high_speed_cruise, long_range_cruise) VALUES (?, ?, ?, ?)",
            (performance.aircraft_id, performance.maximum_range, performance.high_speed_cruise,
             performance.long_range_cruise))
        self.conn.commit()

    def get_performance(self, aircraft_id: int):
        self.cursor.execute("SELECT * FROM Performance WHERE aircraft_id = ?", (aircraft_id,))
        performance = self.cursor.fetchone()
        return performance

    def get_performances(self):
        self.cursor.execute("SELECT * FROM Performance")
        performance = self.cursor.fetchall()
        return performance

    def update_performance(self, performance_id: int, performance: Performance):
        self.cursor.execute(
            "UPDATE Performance SET maximum_range = ?, high_speed_cruise = ?, long_range_cruise = ? WHERE id = ?",
            (performance.maximum_range, performance.high_speed_cruise, performance.long_range_cruise, performance_id))
        self.conn.commit()

    def delete_performance(self, performance_id: int):
        self.cursor.execute("DELETE FROM Performance WHERE id = ?", (performance_id,))
        self.conn.commit()

    # Cabin
    def create_cabin(self, cabin: Cabin):
        self.cursor.execute(
            "INSERT INTO Cabin (aircraft_id, living_areas, num_panoramic_windows, total_interior_length) VALUES (?, ?, ?, ?)",
            (cabin.aircraft_id, cabin.living_areas, cabin.num_panoramic_windows, cabin.total_interior_length))
        self.conn.commit()

    def get_cabin(self, aircraft_id: int):
        self.cursor.execute("SELECT * FROM Cabin WHERE aircraft_id = ?", (aircraft_id,))
        cabin = self.cursor.fetchone()
        return cabin

    def get_cabins(self):
        self.cursor.execute("SELECT * FROM Cabin ")
        cabins = self.cursor.fetchall()
        return cabins

    def update_cabin(self, cabin_id: int, cabin: Cabin):
        self.cursor.execute(
            "UPDATE Cabin SET living_areas = ?, num_panoramic_windows = ?, total_interior_length = ? WHERE id = ?",
            (cabin.living_areas, cabin.num_panoramic_windows, cabin.total_interior_length, cabin_id))
        self.conn.commit()

    def delete_cabin(self, cabin_id: int):
        self.cursor.execute("DELETE FROM Cabin WHERE id = ?", (cabin_id,))
        self.conn.commit()

    # systems
    def create_systems(self, systems: Systems):
        self.cursor.execute("INSERT INTO Systems (aircraft_id, avionics, engines) VALUES (?, ?, ?)",
                            (systems.aircraft_id, systems.avionics, systems.engines))
        self.conn.commit()

    def get_system(self, aircraft_id: int):
        self.cursor.execute("SELECT * FROM Systems WHERE aircraft_id = ?", (aircraft_id,))
        systems = self.cursor.fetchone()
        return systems

    def get_systems(self):
        self.cursor.execute("SELECT * FROM Systems")
        systems = self.cursor.fetchall()
        return systems

    def update_systems(self, systems_id: int, systems: Systems):
        self.cursor.execute("UPDATE Systems SET avionics = ?, engines = ? WHERE id = ?",
                            (systems.avionics, systems.engines, systems_id))
        self.conn.commit()

    def delete_systems(self, systems_id: int):
        self.cursor.execute("DELETE FROM Systems WHERE id = ?", (systems_id,))
        self.conn.commit()

    def query_aircraft_by_performance(self, maximum_range: Optional[float], high_speed_cruise: Optional[float],
                                      long_range_cruise: Optional[float]):
        query = "SELECT a.id, a.name FROM Aircraft a INNER JOIN Performance p ON a.id = p.aircraft_id WHERE"
        conditions = []
        parameters = []

        if maximum_range is not None:
            conditions.append(" p.maximum_range >= ? ")
            parameters.append(maximum_range)

        if high_speed_cruise is not None:
            conditions.append(" p.high_speed_cruise >= ? ")
            parameters.append(high_speed_cruise)

        if long_range_cruise is not None:
            conditions.append(" p.long_range_cruise >= ? ")
            parameters.append(long_range_cruise)

        query += " AND ".join(conditions)
        self.cursor.execute(query, tuple(parameters))
        aircrafts = self.cursor.fetchall()
        return aircrafts

    def query_aircrafts_by_cabin(self, living_areas: int, num_panoramic_windows: int, total_interior_length: float):
        query = "SELECT * FROM Aircraft a INNER JOIN Cabin c ON a.id = c.aircraft_id WHERE 1 = 1"
        params = []

        if living_areas is not None:
            query += " AND c.living_areas >= ?"
            params.append(living_areas)

        if num_panoramic_windows is not None:
            query += " AND c.num_panoramic_windows >= ?"
            params.append(num_panoramic_windows)

        if total_interior_length is not None:
            query += " AND c.total_interior_length >= ?"
            params.append(total_interior_length)

        self.cursor.execute(query, tuple(params))
        aircrafts = self.cursor.fetchall()
        return aircrafts

    def query_aircrafts_by_systems(self, avionics: str, engines: str):
        query = "SELECT * FROM Aircraft a INNER JOIN Systems s ON a.id = s.aircraft_id WHERE 1 = 1"
        params = []

        if avionics is not None:
            query += " AND s.avionics = ?"
            params.append(avionics)

        if engines is not None:
            query += " AND s.engines = ?"
            params.append(engines)

        self.cursor.execute(query, tuple(params))
        aircrafts = self.cursor.fetchall()
        return aircrafts

