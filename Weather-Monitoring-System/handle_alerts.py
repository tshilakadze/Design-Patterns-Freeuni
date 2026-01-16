from abc import ABC, abstractmethod


class AlertHandler(ABC):
    @abstractmethod
    def handle_alert(self, temperature, wind_speed, humidity):
        pass
