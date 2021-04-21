import socket
import time

TELLO = ('192.168.10.1', 8889)
SLEEP_TIME = 3

def init_drone():
    print('==> Connecting to Drone...')

    # create UDP client on PC
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as err:
        print('==> Connection Failed - Socket Error:')
        print(err)
        exit()

    try:
        # send control commands to the drone
        s.sendto(b'command', TELLO)
        time.sleep(SLEEP_TIME)
    except socket.error as err:
        print(err)

    print('==> Connection Established')
    return s


def main():
    # Establish socket connection
    skt = init_drone()

    # Main Loop
    while True:
        cmd = input('D R O N E > ')
        if cmd == '' or cmd == 'exit':
            break
        else:
            skt.sendto(cmd.encode('ascii'), TELLO)
            time.sleep(SLEEP_TIME)
            print('<== Sent')
 
    print('==> Exiting and Landing...')
    time.sleep(SLEEP_TIME)
    skt.sendto(b'land', TELLO)
 
if __name__ == '__main__':
    main()