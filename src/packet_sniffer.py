from scapy.all import *
import time
import datetime

packets = sniff(count=5)

def assemble_stream(packets):
    streams = {}

    for packet in packets:
        if packet.haslayer(TCP) and packet.haslayer(IP):
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport

            timestamp = datetime.datetime.fromtimestamp(
                packet.time
            ).strftime('%Y-%m-%d %H:%M:%S.%f')

            flow_key = {"src_ip": src_ip, "dst_ip": dst_ip, "src_port": src_port, "dst_port": dst_port}

            state = streams.setdefault(flow_key, {
                "timestamps": []
            })

            state["timestamps"].append(timestamp)

    return streams

streams = assemble_stream(packets)
print(streams)