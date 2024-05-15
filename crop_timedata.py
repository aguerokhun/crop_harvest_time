import csv
from fastapi import FastAPI, HTTPException
from datetime import datetime, timedelta
import pandas as pd

app = FastAPI()
df = pd.read_csv("output.csv")

@app.get("harvest_date")
async def get_harvest_date(crop: str, date: str):
    try:
        planting_date = datetime.strptime(planting_date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code= 400, detail = "Invalid Date Format, Use YYYY-MM-DD.")
    
    if crop not in df['CROP']:
        raise HTTPException(status_code= 404, detail = "Crop not found")
    
    days_to_add = df.loc[df['CROP'] == crop, "DAYS"].values[0]
    
    harvest_date = planting_date + timedelta(days=days_to_add)
    
    return {"crop":crop, "planting_date" : planting_date.strftime("%y-%m-%d"), "harvest_date" : harvest_date.strftime("%y-%m-%d")}   
    
