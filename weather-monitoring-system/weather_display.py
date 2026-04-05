from weather_data import WeatherData
from weather_observer import WeatherObserver


class WeatherDisplay(WeatherObserver):
    def update(self, data: WeatherData) -> None:
        print(
            f"WeatherDisplay: "
            f"Temperature={data.temperature}°C, "
            f"Humidity={data.humidity}%, "
            f"Wind={data.wind_speed} km/h"
        )
