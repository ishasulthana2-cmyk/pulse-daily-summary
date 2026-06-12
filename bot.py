print("NEW VERSION")
import requests

def get_weather():
    url = "https://wttr.in/Trivandrum?format=j1"
    response = requests.get(url, timeout=10)
    data = response.json()
    return data["current_condition"][0]["temp_C"]

def get_quote():
    url = "https://zenquotes.io/api/random"
    response = requests.get(url, timeout=10)
    data = response.json()
    return data[0]["q"]

def build_summary():
    weather = get_weather()
    quote = get_quote()

    return f"""
DAILY SUMMARY
================

Temperature: {weather}°C

Quote:
{quote}
"""

if __name__ == "__main__":
    print(build_summary())
