from weather_data import WeatherData
from weather_observer import WeatherObserver


class WeatherStation:
    def __init__(self) -> None:
        self._observers: list[WeatherObserver] = []

    def add_observer(self, observer: WeatherObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: WeatherObserver) -> None:
        self._observers.remove(observer)

    def set_weather(self, data: WeatherData) -> None:
        for observer in self._observers:
            observer.update(data)

