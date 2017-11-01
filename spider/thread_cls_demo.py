#coding:utf8
import threading
import time
import Queue   #线程安全的

class CrawlThread(threading.Thread):
    def __init__(self,thread_name): #初始化方法
        super(CrawlThread, self).__init__() #调用父类初始化方法

        # 自定义初始化属性
        self.thread_name = thread_name
    def run(self): #run方法必须写，启动线程时调用的函数
        print '启动',str(self.thread_name) + '号线程'
        time.sleep(2)

if __name__ == '__main__':
    crawl_list = []
    for i in range(10):
        t = CrawlThread(i)
        t.start()
        crawl_list.append(t)
        print t.is_alive()  # 判断线程是否存活

    for crawl_thread in crawl_list:
        crawl_thread.join()

    print '-' * 200
    for crawl_thread in crawl_list:
        print crawl_thread.is_alive()

