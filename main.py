from fastapi import FastAPI
from datetime import datetime

from utils import fetch_surf_data

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello, World!"}


@app.get("/how-is-the-surf")
def get_surf_sessions():
    return fetch_surf_data("5842041f4e65fad6a7708bca")


@app.get("/how-is-the-surf/{spot_id}")
def get_surf_sessions_by_spot_id(spot_id):
    # Call the pysurfline function to get surf data
    surf_data = fetch_surf_data(spot_id)

    # Return the processed data
    return {"timestamp": datetime.now().isoformat(), "surf_data": surf_data}
