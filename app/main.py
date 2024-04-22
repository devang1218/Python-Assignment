from fastapi import FastAPI, Body, HTTPException, status
from typing import Optional, List
from pydantic import BaseModel
import sqlite3
from math import radians, sin, cos, acos
from database import database

# Define database path
path= "address.db"

db = database(path)

# Address model for data validation
class Address(BaseModel):
    name: str
    street: str
    city: str
    state: str
    zip: str
    latitude: float
    longitude: float

# Get distance model for data validation
class GetDistance(BaseModel):
    lat: float
    lon: float
    distance: float


# utility function to calculate the distance between 2 given coordinates
def calculate_distance(lat1, lon1, lat_lon_list, distance):
    ids = []
    lat1, lon1 = map(radians, [lat1, lon1,])
    for i in lat_lon_list:
        d = 0
        lat2 = i[1]
        lon2 = i[2]

        # Convert degrees to radians
        lat2, lon2 = map(radians, [lat2, lon2])

        # Haversine formula for distance calculation
        d = acos((sin(lat1) * sin(lat2)) + (cos(lat1) * cos(lat2) * cos(lon1 - lon2)))
        r = 6371  # Earth's radius in kilometers

        if round(d * r, 2) < distance:
            ids.append(i[0])
    return ids 

app = FastAPI()

app.add_event_handler("shutdown", db.close_connection)

# Create a new address
@app.post("/addAddress")
def create_address(address: Address):
    # Validate coordinates
    if not (-90 <= address.latitude <= 90) or not (-180 <= address.longitude <= 180):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid coordinates")
    
    try:
        created_address = db.insert_data(address=address)
        print(created_address)
        return created_address
    except sqlite3.Error as e:
        print(f"Error creating address: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

# Update an existing address
@app.put("/addresses/{address_id}")
def update_address(address_id: int, address: Address):
    # Validate coordinates
    if not (-90 <= address.latitude <= 90) or not (-180 <= address.longitude <= 180):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid coordinates")

    try:
        res = db.update_address(address_id, address)
        if res == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Address id not found")
        return {"message": "Address updated successfully"}
    except sqlite3.Error as e:
        print(f"Error updating address: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail= "Internal Server Error")
    
# Update an existing address
@app.delete("/deleteAddress/{address_id}")
def delete_address(address_id: int):
    try:
        res = db.delete_address(address_id)
        print("delete result: ", res)
        if res == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Address id not found")
        return {"message": "Address deleted successfully!"}
    except sqlite3.Error as e:
        print(f"Error deleting address: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail= "Internal Server Error")

# api to calculate distance between two coordinates
@app.post("/getAddressesByDistance")
def get_addresses_within_distance(dist_param: GetDistance):
    if not (-90 <= dist_param.lat <= 90) or not (-180 <= dist_param.lon <= 180) :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid coordinates")

    try:
        lat_lon_list = []
        lat_lon_list = db.get_lat_lon_list()
        if len(lat_lon_list) == 0:
            return "There are no addresses in database to compare with."
        ids = calculate_distance(dist_param.lat, dist_param.lon, lat_lon_list, dist_param.distance)
        if len(ids)==0:
            return "No addresses found in the given range!"
        print(ids)
        res = db.get_addresses(ids)
        return res
    
    except sqlite3.Error as e:
        print(f"Error calculating distance: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
