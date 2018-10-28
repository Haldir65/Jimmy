import os,logging

def renaming_files():
    file_dir = os.path.join(os.getcwd(),'static')
    start_index = 100
    os.chdir(file_dir)
    for index,val in enumerate(os.listdir(os.curdir)):
        print('index %d filename %s' % (index,val))
        if(val.endswith(".jpg")):
            os.rename(val,str((start_index+index))+'.jpg')
        elif(val.endswith(".png")):
            os.rename(val,str((start_index+index))+'.png')
        else:
            logging.error("unrecognized file format!")

    

def main():
    renaming_files()

if __name__ == '__main__':
    main()