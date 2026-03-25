import os
import json
from typing import Dict
from fastmcp import FastMCP
from aiohttp import ClientSession

mcp = FastMCP("mcp-accuweather")
API_KEY = os.getenv("ACCUWEATHER_API_KEY")
API_URL = "http://dataservice.accuweather.com"

@mcp.tool(description="""Get weather conditions for a location.""")
async def get_weather_conditions(location:str) -> Dict:
    async with ClientSession() as session:
        search_location_url = f"{API_URL}/locations/v1/cities/search"
        params = {
            "apikey": API_KEY,
            "q":location,
        }

        async with session.get(search_location_url, params=params) as response:
            locations = await response.json()
            if response.status != 200:
                raise Exception(f"""Error fetching location data: {response.status}, {locations}""")
            if not locations or len(locations) == 0:
                raise Exception("Location not found")
        location_key = locations[0]["Key"]

        current_conditions_url = f"{API_URL}/currentconditions/v1/{location_key}"
        params = {
            "apikey": API_KEY,
            "details": "true",
        }

        async with session.get(current_conditions_url, params=params) as response:
            current_conditions = await response.json()

        if current_conditions and len(current_conditions) > 0:
            current = current_conditions[0] #J
            current_data = {
                "temperature": {
                    "value": current["Temperature"]["Metric"]["Value"],
                    "unit": current["Temperature"]["Metric"]["Unit"]
                },
                "weather_text": current["WeatherText"],
                "relative_humidity": current.get("RelativeHumidity"),
                "precipitation": current.get("HasPrecipitation", False),
                "observation_time": current["LocalObservationDateTime"]
            }
        else:
            current_data = "No current conditions available"

        return { #K
            "location": locations[0]["LocalizedName"], 
            "location_key": location_key, 
            "country": locations[0]["Country"]["LocalizedName"], 
            "current_conditions": current_data,
        }



if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8020, path="/accu-mcp-server")
