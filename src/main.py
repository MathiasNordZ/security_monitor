from CaptureEngine import CaptureEngine

def main():
    captureEngine = CaptureEngine("lo")
    captureEngine.start("tcp")

if __name__ == "__main__":
    main()