import socket, sys
from multiprocessing import Process
from abc import ABC


class Abstract_Chat(ABC):
    @abstractmethod
    def send():
        pass


    @abstractmethod
    def receive():
        pass


    pass


class MainFactory:
    @staticmethod
    def build_client():
        pass

    @staticmethod
    def build_server():
        pass

    @staticmethod
    def build_logger():
        pass

    @staticmethod
    def build_cipher():
        pass

    pass


class Client(Abstract_Chat):
    pass


class Server(Abstract_Chat):
    pass


class Logger:
    pass


class Monitor:
    pass


class UI:
    pass


class Cipher:
    pass


def main():
    pass

