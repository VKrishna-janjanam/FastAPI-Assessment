from fastapi import FastAPI, HTTPException, Query
from typing import Optional
import uvicorn
from database import Database
from models import Aircraft, Performance, Cabin, Systems

app = FastAPI()
db = Database()


# Aircraft
@app.post("/aircrafts")
def create_aircraft(aircraft: Aircraft):
    """
    Method to create the aircraft
    :param aircraft: dict (name)
    :return: dict
    """
    print(aircraft)
    db.create_aircraft(aircraft)
    aircraft_id = db.cursor.lastrowid
    return {"message": "Aircraft created successfully", "aircraft_id": aircraft_id}


@app.get("/aircrafts")
def create_aircraft():
    """
    Method to get all available aircraft information
    :return: list of aircraft
    """
    res = db.get_air_crafts()
    return {"aircrafts": res}


@app.get("/aircrafts/{aircraft_id}")
def read_aircraft(aircraft_id: int):
    """
    Method to get the aircraft details based on aircraft id
    """
    aircraft = db.get_aircraft(aircraft_id)
    if not aircraft:
        raise HTTPException(status_code=404, detail="Aircraft not found")
    return {"aircraft_id": aircraft[0], "name": aircraft[1]}


@app.put("/aircrafts/{aircraft_id}")
def update_aircraft(aircraft_id: int, aircraft: Aircraft):
    """
    Method to update the aircraft details based on aircraft id
    """
    db.update_aircraft(aircraft_id, aircraft)
    return {"message": "Aircraft updated successfully"}


@app.delete("/aircrafts/{aircraft_id}")
def delete_aircraft(aircraft_id: int):
    """
    Method to delete the aircraft details based on aircraft id
    """
    db.delete_aircraft(aircraft_id)
    return {"message": "Aircraft deleted successfully"}


# Performance
@app.post("/performance")
def create_performance(performance: Performance):
    """
    Method to create the performance details for an aircraft
    """
    db.create_performance(performance)
    performance_id = db.cursor.lastrowid
    return {"message": "Performance created successfully", "performance_id": performance_id}


@app.get("/performances")
def get_performances():
    """
    Method to get all available performances information
    :return: list of aircraft
    """
    res = db.get_performances()
    return {"performances": res}


@app.get("/performance/{aircraft_id}")
def read_performance(aircraft_id: int):
    performance = db.get_performance(aircraft_id)
    if not performance:
        raise HTTPException(status_code=404, detail="Performance not found")
    return {
        "aircraft_id": performance[0],
        "maximum_range": performance[1],
        "high_speed_cruise": performance[2],
        "long_range_cruise": performance[3]
    }


@app.put("/performance/{performance_id}")
def update_performance(performance_id: int, performance: Performance):
    db.update_performance(performance_id, performance)
    return {"message": "Performance updated successfully"}


@app.delete("/performance/{performance_id}")
def delete_performance(performance_id: int):
    db.delete_performance(performance_id)
    return {"message": "Performance deleted successfully"}


# Cabin
@app.post("/cabin")
def create_cabin(cabin: Cabin):
    db.create_cabin(cabin)
    return {"message": "Cabin created successfully"}


@app.get("/cabins")
def get_cabins():
    """
    Method to get all available cabins information
    :return: list of aircraft
    """
    res = db.get_cabins()
    return {"cabins": res}


@app.get("/cabin/{aircraft_id}")
def read_cabin(aircraft_id: int):
    cabin = db.get_cabin(aircraft_id)
    if not cabin:
        raise HTTPException(status_code=404, detail="Cabin not found")
    return {
        "aircraft_id": cabin[0],
        "living_areas": cabin[1],
        "num_panoramic_windows": cabin[2],
        "total_interior_length": cabin[3]
    }


@app.put("/cabin/{cabin_id}")
def update_cabin(cabin_id: int, cabin: Cabin):
    db.update_cabin(cabin_id, cabin)
    return {"message": "Cabin updated successfully"}


@app.delete("/cabin/{cabin_id}")
def delete_cabin(cabin_id: int):
    db.delete_cabin(cabin_id)
    return {"message": "Cabin deleted successfully"}


# Systems
@app.post("/systems")
def create_systems(systems: Systems):
    db.create_systems(systems)
    return {"message": "Systems created successfully"}


@app.get("/systems")
def get_systems():
    """
    Method to get all available systems information
    :return: list of aircraft
    """
    res = db.get_systems()
    return {"systems": res}


@app.get("/systems/{aircraft_id}")
def read_systems(aircraft_id: int):
    systems = db.get_system(aircraft_id)
    if not systems:
        raise HTTPException(status_code=404, detail="Systems not found")
    return {
        "aircraft_id": systems[0],
        "avionics": systems[1],
        "engines": systems[2]
    }


@app.put("/systems/{systems_id}")
def update_systems(systems_id: int, systems: Systems):
    db.update_systems(systems_id, systems)
    return {"message": "Systems updated successfully"}


@app.delete("/systems/{systems_id}")
def delete_systems(systems_id: int):
    db.delete_systems(systems_id)
    return {"message": "Systems deleted successfully"}


@app.get("/get_aircrafts_by_performance")
def query_aircrafts_by_performance(
    maximum_range: float = Query(None),
    high_speed_cruise: float = Query(None),
    long_range_cruise: float = Query(None)
):
    """
        Method to query the aircrafts based on the performance values
    """
    aircrafts = db.query_aircraft_by_performance(maximum_range, high_speed_cruise, long_range_cruise)
    return {"aircrafts": aircrafts}


@app.get("/get_aircrafts_by_cabin")
def query_aircrafts_by_cabin(living_areas: int = Query(None),
                             num_panoramic_windows: int = Query(None),
                             total_interior_length: float = Query(None)):
    """
        Method to query the aircrafts based on the cabin values
    """
    aircrafts = db.query_aircrafts_by_cabin(living_areas, num_panoramic_windows, total_interior_length)
    return {"aircrafts": aircrafts}


@app.get("/get_aircrafts_by_system")
def query_aircrafts_by_systems(
    avionics: str = Query(None),
    engines: str = Query(None)
):
    """
        Method to query the aircrafts based on the System values
    """
    aircrafts = db.query_aircrafts_by_systems(avionics, engines)
    return {"aircrafts": aircrafts}


if __name__ == "__main__":
    # uvicorn.run("run:app", host="0.0.0.0", port=8000)
    uvicorn.run("run:app", port=3001)