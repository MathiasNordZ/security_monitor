import time

class PacketWindow:
    def __init__(self, timeframe = 2):
        self.timeframe = timeframe
        self.window_start = time.time()
        self.packets = []

    def create_window(self, packet):
        now = time.time()

        # If window expired, emit it
        if now - self.window_start >= self.timeframe:
            completed_window = {
                "window_start": self.window_start,
                "window_end": self.window_start + self.timeframe,
                "packets": self.packets,
            }

            # Reset window
            self.window_start = now
            self.packets = []

            # Add packet to new window
            self.packets.append(packet)

            return completed_window

        # Otherwise just accumulate
        self.packets.append(packet)
        return None