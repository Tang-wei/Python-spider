#coding:utf8
import threading
import time

def foo1():
    print '开始运行foo1'
    time.sleep(3)
    print '结束运行foo1'
def foo2():
    print '开始运行foo2'
    time.sleep(5)
    print '结束运行foo2'

# 创建一个线程
t1 = threading.Thread(target=foo1)
t2 = threading.Thread(target=foo2)
# 启动线程
start = time.time()
t1.start()
t2.start()
# 如果线程运行中，则阻塞进程（前台进程）
t1.join()
t2.join()

print time.time() - start





