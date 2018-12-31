import socket,select,selectors,sys

class TCPSERVER:

    def __init__(self):
        self.local_addr = "127.0.0.1"
        self.local_port = '1190'
        self.lsock = []
        self.remote_addr = "127.0.0.1"
        self.remote_port = '15000'
        self.msg_queue = {}


    def tcp_server(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.setblocking(0)
            sock.bind((self.local_addr, int(self.local_port)))
            sock.listen(3)
            self.lsock.append(sock)
            print('[*] Listening on {0} {1}'  .format(self.local_addr,self.local_port))
            while True:
                readable, writable, exceptional = select.select(self.lsock, [], [])
                for s in readable:
                    if s == sock:
                        rserver =self.remote_conn()
                        if rserver:
                            client, addr = sock.accept()
                            print('Accepted connection {0} {1}'.format(addr[0], addr[1]))
                            self.store_sock(client, addr, rserver)
                            break
                        else:
                            print('the connection with the remote server can\'t be \
                            established')
                            print('Connection with {} is closed'.format(addr[0]))
                            client.close()
                    data = self.received_from(s, 3)
                    # httpstr = "GET / HTTP/1.1\r\n\/"
                    self.msg_queue[s].send(data)
                    # self.msg_queue[s].send(httpstr)

                    if len(data) == 0:
                        self.close_sock(s)
                        break
                    else:
                        print('Received {} bytes from client '.format(len(data)))
                        self.hexdump(data)
        except KeyboardInterrupt:
            print ('Ending server')        
        except Exception as e:
            print('Failed to listen on {}:{}'.format(self.local_addr, self.local_port))
            print(str(e))
            sys.exit(0)      
        finally:
            sys.exit(0)
            
    def received_from(self, sock, timeout):
        data = ""
        sock.settimeout(timeout)
        try:
            while True:
                data = sock.recv(4096)
                if not data:
                    break
                # data =(b''.join(data)).decode('utf-8')
                print("accepted %s data" % data.decode('utf-8'))
        except Exception as e:
            print(e)
            pass
        return data


    def remote_conn(self):
        try:
            remote_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            remote_sock.connect((self.remote_addr, int(self.remote_port)))
            return remote_sock
        except Exception as e:
            print(e)
            return False

    def store_sock(self, client, addr, rserver):
        self.lsock.append(client)
        self.lsock.append(rserver)
        self.msg_queue[client] =  rserver
        self.msg_queue[rserver] =  client        

    def hexdump(self, data, length=16):
        filter = ''.join([(len(repr(chr(x))) == 3) and chr(x) or '.' for x in range(256)])
        lines = []
        digits = 4 if isinstance(data, str) else 2
        for c in range(0, len(data), length):
            chars = data[c:c+length]
            hex = ' '.join(["%0*x" % (digits, (x)) for x in chars])
            printable = ''.join(["%s" % (((x) <= 127 and filter[(x)]) or '.') for x in chars])
            lines.append("%04x  %-*s  %s\n" % (c, length*3, hex, printable))
        print(''.join(lines))

    def close_sock(self, sock):
        print ('End of connection with {}'.format(sock.getpeername()))
        self.lsock.remove(self.msg_queue[sock])
        self.lsock.remove(self.msg_queue[self.msg_queue[sock]])
        serv = self.msg_queue[sock]
        self.msg_queue[serv].close()
        self.msg_queue[sock].close()
        del self.msg_queue[sock]
        del self.msg_queue[serv]    


TCPSERVER().tcp_server()