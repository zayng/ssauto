# -*- coding: cp936 -*-
from multiprocessing import Process, Queue  
import time
import os
def offer(i):
    #for t in range(100):
    #    print(str(i)+"------"+str(t))
    print("run process: " + str(i))
    os.system("start \"启动测试......\" c:\\a.bat")
    '''
    for i in range(100):  
        queue.put(i)
        time.sleep(1)  
  '''
if __name__ == '__main__':
    #q = Queue()
    print("start testing....")
    for i in range(5):  
        p = Process(target=offer, args=(i,))
        p.start()
        p.join()
    time.sleep(1)
    print('Start successful!!!')