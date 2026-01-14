from ProtocolEnum import Protocol

class NormalizePacket:
    def __init__(self, src_ip, dst_ip, src_port, dst_port, timestamp, protocol, byte_count, sensor):
        self.timestamp = timestamp
        self.sensor = sensor
        self.protocol: Protocol = protocol
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.src_port = src_port
        self.dst_port = dst_port
        self.byte_count = byte_count