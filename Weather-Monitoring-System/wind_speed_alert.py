from handle_alerts import AlertHandler


class WindSpeedAlert(AlertHandler):
    def __init__(self, prev_speed, prev_prev_speed):
        self.name = "WindSpeedAlert"
        self.prev_speed = prev_speed
        self.prev_prev_speed = prev_prev_speed

    def handle_alert(self, temperature, wind_speed, humidity):
        result_bool = False
        if wind_speed > self.prev_speed > self.prev_prev_speed:
            print(
                f"WindSpeedAlert: **Alert! Wind speed is increasing: {self.prev_speed} km/h -> {wind_speed} km/h"
            )
            result_bool = True
        else:
            print("WindSpeedAlert: No alert (No upward trend detected)")
        self.prev_prev_speed = self.prev_speed
        self.prev_speed = wind_speed
        return result_bool
