from pydantic import BaseModel


class Aircraft(BaseModel):
    name: str


class Performance(BaseModel):
    aircraft_id: int
    maximum_range: float
    high_speed_cruise: float
    long_range_cruise: float


class Cabin(BaseModel):
    aircraft_id: int
    living_areas: int
    num_panoramic_windows: int
    total_interior_length: float


class Systems(BaseModel):
    aircraft_id: int
    avionics: str
    engines: str


