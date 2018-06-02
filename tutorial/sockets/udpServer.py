import socket

def Main():
    host = '127.0.0.1'
    port =13000

    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((host,port))

    print('Server started ...')

    while True:
        try:
            data, addr = s.recvfrom(1024) ## 一次接受1024个字节
            data = data.decode('utf-8')

            print('Message from '+str(addr))
            print('From connected user: '+data)

            data = data.upper()

            print('sending: '+data)
            s.sendto(data.encode('utf-8'),addr)
        except Exception:
            print('server shuting down ')
            s.close()


if __name__ == '__main__':
    Main()