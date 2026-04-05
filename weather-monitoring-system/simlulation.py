import random

from humidity_alert import HumidityAlert
from temperature_alert import TemperatureAlert
from weather_data import WeatherData
from weather_display import WeatherDisplay
from weather_station import WeatherStation
from wind_speed_alert import WindSpeedAlert

ADD_PROBABILITY = 0.8
REMOVE_PROBABILITY = 0.5

def simulate() -> None:
    station = WeatherStation()
    station.add_observer(WeatherDisplay())

    alerts = [
        TemperatureAlert(),
        WindSpeedAlert(),
        HumidityAlert(),
    ]

    available_alerts = alerts.copy()
    active_alerts: list = []

    for week in range(1, 21):
        print(f"\n---\nWeek {week}:")
        if available_alerts and random.random() < ADD_PROBABILITY:
            alert = random.choice(available_alerts)
            active_alerts.append(alert)
            available_alerts.remove(alert)
            station.add_observer(alert)
            print(f"Adding: {alert.__class__.__name__}")
        elif active_alerts and random.random() < REMOVE_PROBABILITY:
            alert = random.choice(active_alerts)
            active_alerts.remove(alert)
            available_alerts.append(alert)
            station.remove_observer(alert)
            print(f"Removing: {alert.__class__.__name__}")


        data = WeatherData(
            temperature=random.randint(25, 45),
            humidity=random.randint(60, 95),
            wind_speed=random.randint(10, 35),
        )

        station.set_weather(data)

if __name__ == "__main__":
    simulate()
