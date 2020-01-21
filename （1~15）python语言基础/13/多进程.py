'''
下面的代码执行了毫不相关的两个下载任务，但是必须等待一个文件下载完成后才能开始
下一个下载任务，这并不合理也没有效率
'''
'''
from random import randint
from time import time, sleep


def download_task(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(3, 7)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    download_task('Python从入门到住院.pdf')
    download_task('Peking Hot.avi')
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()

'''
'''
下面代码使用多进程的方式将两个下载任务放到不同的进程中，我们通过Process类创建了进程
对象，通过target参数我们传入一个函数来表示进程启动后要执行的代码，后面的args是一个
元组，它代表了传递给函数的参数。Process对象的start方法用来启动进程，而join方法表示
等待进程执行结束。运行上面的代码可以明显发现两个下载任务“同时”启动了，而且程序的执行
时间将大大缩短，不再是两个任务的时间总和。
'''

'''
from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(3, 7)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    p1 = Process(target=download_task, args=('Python从入门到住院.pdf', ))
    p1.start()
    p2 = Process(target=download_task, args=('Peking Hot.avi', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()
'''

'''
看起来没毛病，但是最后的结果是Ping和Pong各输出了10个，Why？当我们在
程序中创建进程的时候，子进程复制了父进程及其所有的数据结构，每个子进
程有自己独立的内存空间，这也就意味着两个子进程中各有一个counter变量，
所以结果也就可想而知了。要解决这个问题比较简单的办法是使用
multiprocessing模块中的Queue类，它是可以被多个进程共享的队列，底层
是通过管道和信号量（semaphore）机制来实现的，
'''
'''
from multiprocessing import Process
from time import sleep

counter = 0


def sub_task(string):
    global counter
    while counter < 10:
        print(string, end='', flush=True)
        counter += 1
        sleep(0.01)

        
def main():
    Process(target=sub_task, args=('Ping', )).start()
    Process(target=sub_task, args=('Pong', )).start()


if __name__ == '__main__':
    main()
'''
