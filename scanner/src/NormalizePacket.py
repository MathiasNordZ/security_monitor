from datetime import datetime
from scapy.all import IP, TCP, UDP
from PacketWindow import PacketWindow

class NormalizePacket:
    def __init__(self, sensor: str):
        self.sensor = sensor
        self.packet_window = PacketWindow(timeframe=2)

    def normalize(self, pkt):
        if IP not in pkt:
            return None

        if TCP in pkt:
            protocol = "TCP"
            src_port = pkt[TCP].sport
            dst_port = pkt[TCP].dport
        elif UDP in pkt:
            protocol = "UDP"
            src_port = pkt[UDP].sport
            dst_port = pkt[UDP].dport
        else:
            return None

        normalized_packet = {
            "timestamp": datetime.utcfromtimestamp(pkt.time).isoformat() + "Z",
            "sensor": self.sensor,
            "src_ip": pkt[IP].src,
            "dst_ip": pkt[IP].dst,
            "src_port": src_port,
            "dst_port": dst_port,
            "protocol": protocol,
            "byte_count": len(pkt),
        }

        # Add to window and maybe get a completed window back
        completed_window = self.packet_window.create_window(normalized_packet)

        print(completed_window)

        return completed_window