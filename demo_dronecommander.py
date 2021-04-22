import socket
import time

TELLOCMD = ('192.168.10.1', 8889)
TELLOST = ('192.168.10.1', 8890)
TELLOSTR = ('192.168.10.1', 11111)
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
        s.sendto(b'command', TELLOCMD)
        time.sleep(SLEEP_TIME)
    except socket.error as err:
        print(err)

    print('==> Connection Established')
    return s

# list of commands for drone
def help():

    print('''==> commands: 
        1) takeoff
        2) land 
        3) streamon - dont use
        4) streamoff - dont use
        5) emergency*
        6) up x (cm)*
        7) down x (cm)* 
        8) left x (cm)*
        9) right x (cm)*
        10) forward x (cm)*
        11) back x (cm)*
        12) cw x (degress) - rotate clockwise
        13) ccw x (degrees) - rotate counter clockwise
        14) flip x (l,r,f,b)
        15) stop
        16) speed x (0-100 cm/s)*
        17) speed? (receive speed)
        18) battery? (obtain battery percentage)
        19) time? (obtain current flight time)
        20) sn? (obtain serial number of drone)

        * - use with caution''')

def main():
    # Establish socket connection
    skt = init_drone()

    # Main Loop
    while True:

        cmd = input('D R O N E >> ')
        if cmd == '' or cmd == 'exit':
            break
        elif cmd =='help':
            help()
 #  test for state commands on port 8890
 #       elif cmd == 'h': 
 #           skt.sendto(cmd.encode('ascii'), TELLOST)
 #           time.sleep(SLEEP_TIME)
 #           print('<== Sent')
        else:
            skt.sendto(cmd.encode('ascii'), TELLOCMD)
            time.sleep(SLEEP_TIME)
            print('<== Sent')
 
    print('==> Exiting ...')
    
 
if __name__ == '__main__':
    main()