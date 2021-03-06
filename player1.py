from gameboard import *
import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try_again = True
    while try_again:
        try_again = False
        try:
            ip = promptInput("Enter Player 2 ip/name")
            # ip = "192.168.43.143"
            port = promptInput("Enter Player 2 port number")
            # port = 5555
            port = int(port)
            s.connect((ip, port))
            print("connection established")

        except Exception as e:
            print("Connection Failed")
            print("Error: ", e)
            again = promptInput("Would you like to try again? (y/n)")
            if again.lower() != 'n':
                try_again = True
            else:
                sys.exit()

    # connected with socket s

    game = Game('X')
    # game.user_name = 'p1'
    game.disableAll()
    # send user name to player 2
    s.send(game.user_name.encode('utf-8'))
    # get player 2 username:
    op = s.recv(2048).decode('utf-8')
    print(f"player2: {op}")
    game.other_player = op
    game.con = s
    game.myTurn = True
    game.enableAll()
    game.play()

    # start game


if __name__ == "__main__":
    main()
