import unittest

from temperature_alert import TemperatureAlert
from weather_station import WeatherStation


class TestWeatherStation(unittest.TestCase):
    TEMPERATURE = 20
    HUMIDITY = 0.7
    WIND_SPEED = 15
    weather = WeatherStation(TEMPERATURE, WIND_SPEED, HUMIDITY)

    def test_alerts(self):
        weather = self.weather
        self.assertEqual(len(weather.current_alerts), 0)
        temp_alert = TemperatureAlert(20)
        weather.add_alert(temp_alert)
        self.assertEqual(len(weather.current_alerts), 1)
        weather.remove_alert(temp_alert)
        self.assertEqual(len(weather.current_alerts), 0)

    def test_set_weather(self):
        weather = self.weather
        weather.set_weather(
            self.TEMPERATURE + 10,
            self.WIND_SPEED + 5,
            self.HUMIDITY,
        )
        self.assertEqual(weather.temperature, self.TEMPERATURE + 10)
        self.assertEqual(weather.wind_speed, self.WIND_SPEED + 5)
