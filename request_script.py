import socket
import time
import threading

ip = '192.168.10.1'
tello = (ip, 8889)
tello_recive = (ip, 8890)
 
def init_drone():
 
    # create upd client on PC
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as err:
        print(err)
        exit()
 
    try:
        # send control commands to the drone
        s.sendto(b'command', tello)
        time.sleep(5)
    except socket.error as err:
        print(err)

# create a UDP server on comp

host = '127.0.0.1'
host_port = 8890
locaddr = (host,host_port)

# Create a UDP socket
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = (ip, 8889)

s2.bind(locaddr)

def recv():
    count = 0
    while True: 
        try:
            data, server = s2.recvfrom(1518)
            print(data.decode(encoding='utf8',errors='strict'))
        except Exception:
            print ('\nExit . . .\n')
            break

#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


def takeoff(s):
    s.sendto(b'takeoff', tello)
    time.sleep(10)
 
def rotate90(s):
    s.sendto(b'cw 90', tello)
    time.sleep(10)
 
def flip_left(s):
    s.sendto(b'flip l', tello)
    time.sleep(10)

def speed(s2):
    s.sendto(b'speed?', tello_recive)
    time.sleep(5)

def battery(s2):
    s.sendto(b'battery?', tello_recive)
    time.sleep(5)

def sdk(s2):
    s.sendto(b'sdk?', tello_recive)
    time.sleep(5)


def land(s):
    s.sendto(b'land', tello)
    time.sleep(5)

def main():
    s = init_drone()
 
    takeoff(s)

    speed(s)

    battery(s)

    sdk(s)

#    rotate90(s)

#    flip_left(s)
 
    land(s)
 
if __name__ == '__main__':
    main()
