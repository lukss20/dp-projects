from abc import ABC, abstractmethod

from weather_data import WeatherData


class WeatherObserver(ABC):
    @abstractmethod
    def update(self, data: WeatherData) -> None:
        pass
