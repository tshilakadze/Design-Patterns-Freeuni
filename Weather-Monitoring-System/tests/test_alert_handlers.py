import unittest

from humidity_alert import HumidityAlert
from temperature_alert import TemperatureAlert
from weather_station import WeatherStation
from wind_speed_alert import WindSpeedAlert
import sys


class TestAlertHandler(unittest.TestCase):
    TEMPERATURE = 20
    HUMIDITY = 0.7
    WIND_SPEED = 15
    weather = WeatherStation(TEMPERATURE, WIND_SPEED, HUMIDITY)

    TEMPERATURE_THRESHOLD = 30
    HUMIDITY_THRESHOLD = 0.75
    WIND_SPEED_FIRST = WIND_SPEED + 2
    WIND_SPEED_SECOND = WIND_SPEED + 3
    WIND_SPEED_THIRD = WIND_SPEED

    def test_temperature_alert(self):
        weather = self.weather
        temperature_alert = TemperatureAlert(self.TEMPERATURE_THRESHOLD)
        self.assertFalse(
            temperature_alert.handle_alert(
                weather.temperature, weather.wind_speed, weather.humidity
            )
        )
        weather.set_weather(
            self.TEMPERATURE_THRESHOLD - 1, weather.wind_speed, weather.humidity
        )
        self.assertFalse(
            temperature_alert.handle_alert(
                weather.temperature, weather.wind_speed, weather.humidity
            )
        )
        weather.set_weather(
            self.TEMPERATURE_THRESHOLD + 1, weather.wind_speed, weather.humidity
        )
        self.assertTrue(
            temperature_alert.handle_alert(
                weather.temperature, weather.wind_speed, weather.humidity
            )
        )

    def test_wind_speed(self):
        weather = self.weather
        wind_speed_alert = WindSpeedAlert(sys.maxsize, sys.maxsize)
        self.assertFalse(
            wind_speed_alert.handle_alert(
                weather.temperature, weather.wind_speed, weather.humidity
            )
        )
        weather.set_weather(self.TEMPERATURE, self.WIND_SPEED_FIRST, weather.humidity)
        self.assertFalse(
            wind_speed_alert.handle_alert(
                weather.temperature, weather.wind_speed, weather.humidity
            )
        )
        weather.set_weather(self.TEMPERATURE, self.WIND_SPEED_SECOND, weather.humidity)
        self.assertTrue(
            wind_speed_alert.handle_alert(
                weather.temperature, weather.wind_speed, weather.humidity
            )
        )
        weather.set_weather(self.TEMPERATURE, self.WIND_SPEED_THIRD, weather.humidity)
        self.assertFalse(
            wind_speed_alert.handle_alert(
                weather.temperature, weather.wind_speed, weather.humidity
            )
        )

    def test_humidity_alert(self):
        weather = self.weather
        humidity_alert = HumidityAlert(self.HUMIDITY_THRESHOLD)
        self.assertFalse(
            humidity_alert.handle_alert(
                weather.temperature, weather.wind_speed, weather.humidity
            )
        )

        weather.set_weather(
            self.TEMPERATURE, weather.wind_speed, self.HUMIDITY_THRESHOLD - 0.1
        )
        self.assertFalse(
            humidity_alert.handle_alert(
                weather.temperature, weather.wind_speed, weather.humidity
            )
        )

        weather.set_weather(
            self.TEMPERATURE, weather.wind_speed, self.HUMIDITY_THRESHOLD + 0.1
        )
        self.assertTrue(
            humidity_alert.handle_alert(
                weather.temperature, weather.wind_speed, weather.humidity
            )
        )
