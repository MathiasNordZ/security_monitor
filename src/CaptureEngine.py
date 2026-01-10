from scapy.all import sniff, TCP, IP

class CaptureEngine:
    def __init__(self,  interface: str):
        self.interface = interface
        self.running = False

    def _stop_filter(self, pkt):
        return not self.running

    def start(self, callback_func, bpf_filter = None):
        self.running = True
        return sniff(prn=callback_func, iface=self.interface, filter=bpf_filter, stop_filter=self._stop_filter)

    def stop(self):
        self.running = False