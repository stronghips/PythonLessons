import requests

lat, lon = 37.9838, 23.7275  # Athens

resp = requests.get("https://api.sunrise-sunset.org/json", params={
    "lat": lat,
    "lng": lon,
    "date": "2025-08-16",
    "formatted": 0   # returns ISO times in UTC
})

data = resp.json()
print("Solar noon (UTC):", data["results"]["solar_noon"])
