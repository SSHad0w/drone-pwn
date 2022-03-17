import socket
import time
import sys
import threading
import argparse

host = ''
port = 9000
LOCADDR = (host, port)
TELLOCMD = ('192.168.10.1', 8889)
TELLOST = ('192.168.10.1', 8890)
TELLOSTR = ('192.168.10.1', 11111)
SLEEP_TIME = 4.5
SOK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def parse_args():
    parser = argparse.ArgumentParser(description="Drone Commander")
    parser.add_argument("-helpme", "--helpme", type=str, metavar="", required=False, help="help menu")
    
    parser.parse_args()

def init_drone():

    print('==> Connecting to Drone...')

    #create UDP client on PC
    SOK.bind(LOCADDR)
    #display port on the local address the socket binded to 
    print('socket binded to: ', port)
    

    try:
        SOK.sendto(b'command', TELLOCMD)
        time.sleep(SLEEP_TIME)
    except socket.error as err:
        print(err)

    recvThread = threading.Thread(target=recv)
    recvThread.start()

    print('==> Connection Established')


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

#receive method to receive the repsonse from the drone
def recv():

    while True: 
        try:
            data, server = SOK.recvfrom(3000)
            #decode and print response from drone
            print(data.decode('ascii'))
        except socket.error as exc:
                print ("Caught exception socket.error : %s" % exc)


def main():

    args = parse_args()

    # Establish socket connection
    init_drone()

    # Main Loop
    while True:

        cmd = input('D R O N E >> ')
        if cmd == 'exit':
            break
            exit(0)
        elif cmd =='help':
            help()
        else:
            SOK.sendto(cmd.encode('ascii'), TELLOCMD)
            time.sleep(SLEEP_TIME)
            print('<== Sent')
 
    print('==> Exiting ...')
    
 
if __name__ == '__main__':
    main()
