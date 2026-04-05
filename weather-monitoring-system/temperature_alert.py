import random

from weather_data import WeatherData
from weather_observer import WeatherObserver


class TemperatureAlert(WeatherObserver):
    def __init__(self) -> None:
        self._threshold = random.randint(30, 35)

    def update(self, data: WeatherData) -> None:
        if data.temperature > self._threshold:
            print(
                f"TemperatureAlert: ALERT! "
                f"{data.temperature}°C > {self._threshold:.1f}°C"
            )
        else:
            print("TemperatureAlert : No alert")