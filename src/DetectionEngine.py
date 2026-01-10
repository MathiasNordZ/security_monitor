import logging
from datetime import datetime, timedelta
from scapy.all import IP

class DetectionEngine:
    def __init__(self):
        self.packet_count = 0
        self.packet_sizes = []
        self.last_log_time = None
        self.log_cooldown = timedelta(seconds=10)
        self._log_configured = False

    def log_config(self):
        if not self._log_configured:
            logging.basicConfig(
                filename="ids_logs.log",
                level=logging.WARNING,
                format="%(asctime)s - %(message)s"
            )
            self._log_configured = True

    def detector(self, packet):
        try:
            if not packet.haslayer(IP):
                return

            self.log_config()

            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            packet_size = len(packet)

            self.packet_sizes.append(packet_size)
            self.packet_count += 1

            suspicious = (
                self.packet_count > 5
                and len(set(self.packet_sizes[-5:])) == 1
            )

            now = datetime.now()

            if suspicious:
                if (
                    self.last_log_time is None
                    or now - self.last_log_time >= self.log_cooldown
                ):
                    logging.warning(
                        f"Suspiciously repetitive traffic detected from "
                        f"{ip_src} to {ip_dst}"
                    )
                    self.last_log_time = now

        except Exception:
            logging.exception("DetectionEngine error")
