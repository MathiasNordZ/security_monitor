import requests
from NormalizePacket import NormalizePacket

def sendNormalizedPacket(normalizer: NormalizePacket, apiUrl: str):
    def callback(pkt):
        if not normalizer or not apiUrl:
            print("Error with provided parameter(s)!")
            return

        normalized_packet = normalizer.normalize(pkt)
        if not normalized_packet:
            return

        try:
            res = requests.post(apiUrl, json=normalized_packet, timeout=3)
            if res.ok:
                print("POST was successful.")
            else:
                print(f"POST failed with status {res.status_code}: {res.text}")
        except requests.RequestException as exc:
            print(f"POST failed: {exc}")

    return callback
