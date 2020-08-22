from gameboard import *
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
port = 5555

try:
    s.bind((IPAddr, port))
    print(f"connect to IP:{IPAddr} Port: {port}")

    # start listning
    s.listen(1)
    # accept a connection
    c, addr = s.accept()

    print(f"Connected to {addr}")

    game = Game('O')
    game.disableAll()
    # game.user_name = 'p2'

    # receive player 1 username
    other_name = c.recv(2048).decode('utf-8')
    print(f"player1: {other_name}")
    game.other_player = other_name
    # send my username
    c.send(game.user_name.encode('utf-8'))
    game.con = c
    game.myTurn = False
    game.click()
    game.play()

except socket.error as e:
    print(e)
    sys.exit()

