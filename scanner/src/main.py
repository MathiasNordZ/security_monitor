from CaptureEngine import CaptureEngine
from DetectionEngine import DetectionEngine

def main():
    captureEngine = CaptureEngine("lo")
    detectionEngine = DetectionEngine()
    
    callback = detectionEngine.detector
    captureEngine.start(callback_func=callback, bpf_filter="ip")

if __name__ == "__main__":
    main()