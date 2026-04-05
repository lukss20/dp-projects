import random

from weather_data import WeatherData
from weather_observer import WeatherObserver


class HumidityAlert(WeatherObserver):
    def __init__(self) -> None:
        self._threshold = random.randint(70, 85)

    def update(self, data: WeatherData) -> None:
        if data.humidity > self._threshold:
            print(
                f"HumidityAlert: ALERT! "
                f"{data.humidity}% > {self._threshold:.1f}%"
            )
        else:
            print("HumidityAlert: No alert")