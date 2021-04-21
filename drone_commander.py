import socket
import time

TELLO = ('192.168.10.1', 8889)
SLEEP_TIME = 4.5

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

def help():

    print('''==> commands: 
        1) takeoff
        2) land 
        3) streamon
        4) streamoff
        5) emergency*
        6) up x(cm)*
        7) down xc(m)* 
        8) left x(cm)*
        9) right x(cm)*
        10) forward x(cm)*
        11) back x*
        12) cw x(degress) - rotate clockwise
        13) ccw x(degrees) - rotate counter clockwise
        14) flip x(l,r,f,b)

        * - use with caution''')

def main():
    # Establish socket connection
    skt = init_drone()

    # Main Loop
    while True:

        cmd = input('D R O N E > ')
        if cmd == '' or cmd == 'exit':
            break
        elif cmd =='help':
            help()
        else:
            skt.sendto(cmd.encode('ascii'), TELLO)
            time.sleep(SLEEP_TIME)
            print('<== Sent')
 
    print('==> Exiting ...')
    
 
if __name__ == '__main__':
    main()