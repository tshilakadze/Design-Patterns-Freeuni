from handle_alerts import AlertHandler


class WeatherStation:
    def __init__(self, temperature, wind_speed, humidity):
        self.temperature = temperature
        self.wind_speed = wind_speed
        self.humidity = humidity
        self.current_alerts = []

    def trigger_alerts(self):
        for alert in self.current_alerts:
            alert.handle_alert(self.temperature, self.wind_speed, self.humidity)

    def set_weather(self, temperature, wind_speed, humidity):
        self.temperature = temperature
        self.wind_speed = wind_speed
        self.humidity = humidity
        self.trigger_alerts()

    def add_alert(self, alert):
        self.current_alerts.append(alert)

    def remove_alert(self, alert):
        self.current_alerts.remove(alert)
