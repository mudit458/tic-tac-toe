from gameboard import *
import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = promptInput("Enter Other player ip/name")
    port = promptInput("Enter Other player port")


if __name__ == "__main__":
    main()