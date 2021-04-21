import socket
import time



tello = ('192.168.10.1', 8889)
 
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
 
    return s

def flyforward(s):
    s.sendto(b'forward 15',tello)
    time.sleep(10)


def takeoff(s):
    s.sendto(b'takeoff', tello)
    time.sleep(10)
 
def rotate90(s):
    s.sendto(b'cw 90', tello)
    time.sleep(10)
 
def flip_left(s):
    s.sendto(b'flip l', tello)
    time.sleep(10)
 
def land(s):
    s.sendto(b'land', tello)
    time.sleep(5)
 
def main():
    s = init_drone()
 
    takeoff(s)

    flyfoward(s)
 
    rotate90(s)
 
    flip_left(s)
 
    land(s)
 
if __name__ == '__main__':
    main()
