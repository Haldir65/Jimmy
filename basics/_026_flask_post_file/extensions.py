import os
import logging
from io import BytesIO



def save_file_to_disk(data,filename):
   cwd = os.path.abspath(os.path.curdir)
   with open(os.path.join(cwd,filename),"wb") as f:
       print(data)
       logging.error('size %d' % len(data))
       num_written = f.write(data);
       logging.error('write file finished %d' % num_written)

