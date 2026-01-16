from handle_alerts import AlertHandler


class HumidityAlert(AlertHandler):
    def __init__(self, humidity_threshold):
        self.name = "HumidityAlert"
        self.humidity_threshold = humidity_threshold

    def handle_alert(self, temperature, wind_speed, humidity):
        if humidity > self.humidity_threshold:
            print(
                f"HumidityAlert: **Alert! Humidity exceeded {self.humidity_threshold}: {humidity}%"
            )
            return True
        else:
            print("HumidityAlert: No Alert (Did Not Exceed Threshold).")
            return False
