from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from datetime import datetime


def get_protocol(packet):

    if packet.haslayer(TCP):
        return "TCP"

    elif packet.haslayer(UDP):
        return "UDP"

    elif packet.haslayer(ICMP):
        return "ICMP"

    else:
        return "OTHER"


def process_packet(packet):

    print("\n" + "=" * 60)
    print("PACKET CAPTURED")
    print("=" * 60)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Time: {timestamp}")

    if packet.haslayer(IP):

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        print(f"Source IP      : {src_ip}")
        print(f"Destination IP : {dst_ip}")

        protocol = get_protocol(packet)
        print(f"Protocol       : {protocol}")

        if packet.haslayer(TCP):

            print(f"Source Port    : {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")

        elif packet.haslayer(UDP):

            print(f"Source Port    : {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")

        payload = bytes(packet.payload)

        if payload:

            print(f"Payload Size   : {len(payload)} bytes")
            print(f"Payload Preview: {payload[:50]}")

    else:
        print("Non-IP Packet")


def main():

    print("=" * 60)
    print("NETWORK PACKET SNIFFER")
    print("=" * 60)
    print("Starting capture...\n")

    sniff(
        prn=process_packet,
        store=False
    )


if __name__ == "__main__":
    main()
