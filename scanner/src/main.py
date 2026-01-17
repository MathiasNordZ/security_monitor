from CaptureEngine import CaptureEngine
from NormalizePacket import NormalizePacket
from Request import sendNormalizedPacket

def main():
    interface = "en0"
    captureEngine = CaptureEngine(interface)
    normalizer = NormalizePacket(sensor=interface)
    callback = sendNormalizedPacket(normalizer=normalizer, apiUrl="http://localhost:8000/api/packets")

    captureEngine.start(callback_func=callback, bpf_filter="ip")

if __name__ == "__main__":
    main()
