from handle_alerts import AlertHandler


class DisplayWeather(AlertHandler):
    def handle_alert(self, temperature, wind_speed, humidity):
        print(
            f"WeatherDisplay: Showing Temperature = {temperature}°C, "
            f"Humidity = {humidity}%, "
            f"Wind Speed = {wind_speed} km/h"
        )
        return True
