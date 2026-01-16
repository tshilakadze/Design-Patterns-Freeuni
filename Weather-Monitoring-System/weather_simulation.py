import random
import sys


from humidity_alert import HumidityAlert
from temperature_alert import TemperatureAlert
from weather_display import DisplayWeather
from weather_station import WeatherStation
from wind_speed_alert import WindSpeedAlert

STARTING_TEMPERATURE = 25
MIN_TEMPERATURE = 10
MAX_TEMPERATURE = 45
MIN_TEMPERATURE_THRESHOLD = 25
STARTING_WIND_SPEED = 12
MIN_WIND_SPEED = 5
MAX_WIND_SPEED = 35
STARTING_HUMIDITY = 60
MIN_HUMIDITY = 0
MIN_HUMIDITY_THRESHOLD = 50
MAX_HUMIDITY = 99

NUMBER_OF_UPDATES = 30


class WeatherSimulation:
    def launch_simulation(self):
        weather = WeatherStation(
            STARTING_TEMPERATURE, STARTING_WIND_SPEED, STARTING_HUMIDITY
        )
        weather.add_alert(DisplayWeather())
        temperature_threshold = random.randint(
            MIN_TEMPERATURE_THRESHOLD, MAX_TEMPERATURE
        )
        humidity_threshold = (
            random.randint(MIN_HUMIDITY_THRESHOLD, MAX_HUMIDITY) / 100.0
        )
        # print("Temperature threshold: " + str(temperature_threshold))
        # print("Humidity threshold: " + str(humidity_threshold))
        temperature_alert = TemperatureAlert(temperature_threshold)
        humidity_alert = HumidityAlert(humidity_threshold)
        wind_speed_alert = WindSpeedAlert(sys.maxsize, sys.maxsize)
        optional_alerts = [
            temperature_alert,
            humidity_alert,
            wind_speed_alert,
        ]
        current_alerts = []
        print("Week 1:")
        weather.trigger_alerts()
        for i in range(NUMBER_OF_UPDATES):
            print(f"\nWeek {i + 2}:")

            if random.randint(0, 1) == 1:
                alert_to_add = random.choice(optional_alerts)
                if alert_to_add not in current_alerts:
                    weather.add_alert(alert_to_add)
                    current_alerts.append(alert_to_add)
                    print("Adding: ", alert_to_add.name)

            new_temperature = random.randint(MIN_TEMPERATURE, MAX_TEMPERATURE)
            new_wind_speed = random.randint(MIN_WIND_SPEED, MAX_WIND_SPEED)
            new_humidity = random.randint(MIN_HUMIDITY, MAX_HUMIDITY) / 100.0
            weather.set_weather(new_temperature, new_wind_speed, new_humidity)

            if random.randint(0, 1) == 1:
                if len(current_alerts) > 0:
                    alert_to_remove = random.choice(current_alerts)
                    current_alerts.remove(alert_to_remove)
                    weather.remove_alert(alert_to_remove)
                    print("Removing: ", alert_to_remove.name)


if __name__ == "__main__":
    sim = WeatherSimulation()
    sim.launch_simulation()
