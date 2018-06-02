import threading
import time

class AsyncWrite(threading.Thread):
    def __init__(self,text,out):
        threading.Thread.__init__(self)
        self.text=text
        self.out=out


    def run(self):
        with open(self.out,"a") as f:
            f.write(self.text+'\n')
            time.sleep(2)
            print("Finished Background File Write to "+self.out)

def Main():
    message = input("Enter a String to Store: ")
    background = AsyncWrite(message,"out.txt")
    background.start()
    print("The program continue while it writes in another thread")
    print("100 + 400 ",100+400)

    background.join()## it will sit here until background is done,when it's done ,it will continue
    print("Waited until thread was completed")


if __name__ == '__main__':
    Main()