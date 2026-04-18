# Python 3.12+
import psutil
from dataclasses import dataclass

@dataclass(frozen=True)
class SystemStatus:
    cpu_usage: float
    ram_usage: float
    battery: int | None

class SystemMonitor:
    """Monitora recursos de hardware em tempo real."""

    def get_report(self) -> SystemStatus:
        cpu = psutil.cpu_percent(interval=0.1)
        ram = psutil.virtual_memory().percent
        battery_data = psutil.sensors_battery()
        battery_percent = int(battery_data.percent) if battery_data else None
        
        return SystemStatus(cpu_usage=cpu, ram_usage=ram, battery=battery_percent)