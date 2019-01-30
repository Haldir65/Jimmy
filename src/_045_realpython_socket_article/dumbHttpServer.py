import logging,socket,time,sys,selectors,signal,os

logging.getLogger().setLevel(logging.INFO)
sel = selectors.DefaultSelector()

lyrics = "wrk is a modern HTTP benchmarking tool capable of generating significant load when run on a single multi-core CPU. It combines a multithreaded design with scalable event notification systems such as epoll and kqueue."

response = "HTTP/1.1 200 OK\n\rDate: Wed, 30 Jan 2019 07:37:30 GMT\r\n"\
"Server: Apache\r\n"\
"Last-Modified: Wed, 30 Jan 2019 07:37:30 GMT\r\n"\
"ETag: '1d0325-2470-40f0276f'\r\n"\
"Accept-Ranges: bytes\r\nContent-Length: {0}\r\nConnection: close\r\nContent-Type: application/json\r\n\r\n"

def genneateresponse(addr , storage):
    return response.format(len(lyrics.encode()))+lyrics+"\r\n\r\n"

class DataWrapper:
    def __init__(self,addr):
        self.addr = addr[0]
        self.port = addr[1]
        self.storage = []



def readConfiguration(signalNumber, frame):  
    print ('(SIGHUP) reading configuration')
    return

def terminateProcess(signalNumber, frame):  
    print ('(SIGTERM) terminating the process')
    sys.exit()

def receiveSignal(signalNumber, frame):  
    print('Received:', signalNumber)
    return

def register_signal():
    signal.signal(signal.SIGHUP, readConfiguration)
    signal.signal(signal.SIGINT, terminateProcess)
    signal.signal(signal.SIGQUIT, receiveSignal)
    signal.signal(signal.SIGILL, receiveSignal)
    signal.signal(signal.SIGTRAP, receiveSignal)
    signal.signal(signal.SIGABRT, receiveSignal)
    signal.signal(signal.SIGBUS, receiveSignal)
    signal.signal(signal.SIGFPE, receiveSignal)
    #signal.signal(signal.SIGKILL, receiveSignal)
    signal.signal(signal.SIGUSR1, receiveSignal)
    signal.signal(signal.SIGSEGV, receiveSignal)
    signal.signal(signal.SIGUSR2, receiveSignal)
    signal.signal(signal.SIGPIPE, receiveSignal)
    signal.signal(signal.SIGALRM, receiveSignal)
    signal.signal(signal.SIGTERM, terminateProcess)

def connect_incoming(sock):
    conn ,addr = sock.accept() ## 这个addr是一个tuple ('127.0.0.1', 41654)
    # print("accecpted connection from ", addr)
    conn.setblocking(False)    
    data = DataWrapper(addr)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn , events, data=data)

def read_or_write_to_sock(key,mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        try:
            recv_data = sock.recv(1024) ## should be ready to read
            if recv_data:
                # data.storage.append(recv_data)
                request = recv_data.decode('utf-8')
                array = request.split(' ')
                if array:
                    if array[0] == 'GET':
                        ## This is get request
                    #    print("you are requesting %s " % array[1] )
                       data.storage.append(array[1])
            else:
                print("closing connection to ",data.addr)
                # sel.unregister(sock)
        except ConnectionResetError as e:
            logging.error(e)
            print("closing connection to ",data.addr)
            sel.unregister(sock)
        except BrokenPipeError as e1:    
            logging.error(e1)
            print("closing connection to ",data.addr)
            sel.unregister(sock)

    if mask & selectors.EVENT_WRITE:
        content = genneateresponse(data.addr,data.storage).encode('utf-8')
        try:
            total_len = len(content)
            sent = 0
            sock.sendall(content)
            # while(sent < total_len):
            #     sent += sock.send(content[total_len-sent]) ## should be ready to write
            #     print("sendout %d bytes " % sent)
            # print(content.decode('utf-8'))
            sel.unregister(sock)
            # sock.close()
        except BrokenPipeError as e:
            logging.error(e)
        except ConnectionResetError as e1:
            logging.error(e1)    




def serverForever():
    host, port = sys.argv[1], int(sys.argv[2])
    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lsock.bind((host, port))
    lsock.listen()
    print("listening on", (host, port))
    lsock.setblocking(False)
    sel.register(lsock, selectors.EVENT_READ, data=None)
    try:
        while True:
            events = sel.select(timeout=None)
            for key, mask in events:
                if key.data is None:
                    connect_incoming(key.fileobj)
                else:
                    read_or_write_to_sock(key, mask)
    except KeyboardInterrupt:
        print("caught keyboard interrupt, exiting")
    finally:
        sel.close()

def main():
    if len(sys.argv) !=3:
        print("usage: ", sys.argv[0], "<host> <port>")
        sys.exit(1)
    register_signal()        
    serverForever()        
   

if __name__ == "__main__":
    main()