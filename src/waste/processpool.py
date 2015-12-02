from multiprocessing import Pool
from time import sleep
import os
def f(x):
    os.system("start c:\\a.bat")
    sleep(1)


def main():
    pool = Pool(processes=3)    # set the processes max number 3
    for i in range(11,30):
        result = pool.apply_async(f, (i,))
    pool.close()
    pool.join()
    if result.successful():
        print('successful')


if __name__ == "__main__":
    main()
