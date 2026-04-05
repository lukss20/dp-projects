from weather_data import WeatherData
from weather_observer import WeatherObserver


class WindSpeedAlert(WeatherObserver):
    def __init__(self) -> None:
        self._previous: float | None = None

    def update(self, data: WeatherData) -> None:
        if self._previous is not None:
            if data.wind_speed > self._previous:
                print(
                    f"WindSpeedAlert: ALERT! "
                    f"{self._previous} → {data.wind_speed}"
                )
            else:
                print("WindSpeedAlert: No alert")
        self._previous = data.wind_speed
