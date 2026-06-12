import requests

def get_weather():
    url = "https://wttr.in/Trivandrum?format=j1"

    response = requests.get(url, timeout=10)

    data = response.json()

    temp = data["current_condition"][0]["temp_C"]

    return temp


def get_quote():
    url = "https://zenquotes.io/api/random"

    response = requests.get(url, timeout=10)

    data = response.json()

    quote = data[0]["q"]

    return quote


def build_summary():
    weather = get_weather()
    quote = get_quote()

    summary = f"""
DAILY SUMMARY
====================

Temperature: {weather}°C

Quote:
{quote}
"""

    return summary


print(build_summary())
