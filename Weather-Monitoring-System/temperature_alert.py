class TemperatureAlert:
    def __init__(self, temperature_threshold):
        self.name = "TemperatureAlert"
        self.temperature_threshold = temperature_threshold

    def handle_alert(self, temperature, wind_speed, humidity):
        if temperature > self.temperature_threshold:
            print(
                f"TemperatureAlert: **Alert! Temperature exceeded {self.temperature_threshold}°C: {temperature}°C"
            )
            return True
        else:
            print("TemperatureAlert: No Alert (Did Not Exceed Threshold).")
            return False
