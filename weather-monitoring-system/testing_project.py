import pytest
from weather_data import WeatherData
from weather_station import WeatherStation
from weather_display import WeatherDisplay
from temperature_alert import TemperatureAlert
from humidity_alert import HumidityAlert
from wind_speed_alert import WindSpeedAlert


def test_temperature_alert(capsys):
    alert = TemperatureAlert()
    data = WeatherData(temperature=0, humidity=50, wind_speed=10)
    alert.update(data)
    captured = capsys.readouterr()
    assert "No alert" in captured.out
    data2 = WeatherData(temperature=100, humidity=50, wind_speed=10)
    alert.update(data2)
    captured = capsys.readouterr()
    assert "ALERT!" in captured.out


def test_humidity_alert(capsys):
    alert = HumidityAlert()
    data = WeatherData(temperature=30, humidity=0, wind_speed=10)
    alert.update(data)
    captured = capsys.readouterr()
    assert "No alert" in captured.out
    data2 = WeatherData(temperature=30, humidity=100, wind_speed=10)
    alert.update(data2)
    captured = capsys.readouterr()
    assert "ALERT!" in captured.out


def test_wind_speed_alert(capsys):
    alert = WindSpeedAlert()
    alert.update(WeatherData(30, 50, 10))
    alert.update(WeatherData(30, 50, 15))
    data = WeatherData(30, 50, 20)
    alert.update(data)
    captured = capsys.readouterr()
    assert "ALERT!" in captured.out


def test_weather_display_shows_weather(capsys):
    display = WeatherDisplay()
    data = WeatherData(temperature=25, humidity=60, wind_speed=15)
    display.update(data)
    captured = capsys.readouterr()
    assert "WeatherDisplay" in captured.out


def test_weather_station_notifies_all(capsys):
    station = WeatherStation()
    display = WeatherDisplay()
    temp_alert = TemperatureAlert()
    humidity_alert = HumidityAlert()
    wind_alert = WindSpeedAlert()
    wind_alert.update(WeatherData(30, 50, 10))
    wind_alert.update(WeatherData(30, 50, 15))
    station.add_observer(display)
    station.add_observer(temp_alert)
    station.add_observer(humidity_alert)
    station.add_observer(wind_alert)
    data = WeatherData(temperature=100, humidity=100, wind_speed=20)
    station.set_weather(data)
    captured = capsys.readouterr()
    assert "WeatherDisplay" in captured.out
    assert "TemperatureAlert: ALERT!" in captured.out
    assert "HumidityAlert: ALERT!" in captured.out
    assert "WindSpeedAlert: ALERT!" in captured.out


def test_add_remove_observers():
    station = WeatherStation()
    temp_alert = TemperatureAlert()
    wind_alert = WindSpeedAlert()
    station.add_observer(temp_alert)
    station.add_observer(wind_alert)
    assert temp_alert in station._observers
    assert wind_alert in station._observers
    station.remove_observer(temp_alert)
    assert temp_alert not in station._observers
    assert wind_alert in station._observers
