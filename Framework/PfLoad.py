#coding=utf-8

import time
import datetime as datetime
import threading

# 多线程：性能测试
def loadTest(request, nub, loop, ThinkTime):
    myreq = request
    threads = []
    starttime = datetime.datetime.now()
    print "request start time %s" % starttime
    for i in range(1, nub + 1):
        t = threading.Thread(target=myreq.req, args=(loop,))
        threads.append(t)
    for t in threads:
        time.sleep(ThinkTime)
        # print "thread %s" %t #打印线程
        t.setDaemon(True)
        t.start()
    t.join()
    endtime = datetime.datetime.now()
    print "request end time %s" % endtime
    time.sleep(3)
    avTime = float(sum(myreq.times)) / float(len(myreq.times))
    AverageTime = "{:.3f}".format(avTime)  # 计算数组的平均值，保留3位小数
    print "Average Response Time %s ms" % AverageTime  # 打印平均响应时间
    usetime = str(endtime - starttime)
    hour = usetime.split(':').pop(0)
    minute = usetime.split(':').pop(1)
    second = usetime.split(':').pop(2)
    totaltime = float(hour) * 60 * 60 + float(minute) * 60 + float(second)  # 计算总的思考时间+请求时间
    print "Concurrent processing %s" % (nub * loop)  # 打印并发数
    print "use total time %s s" % (totaltime - float(nub * ThinkTime))  # 打印总共消耗的时间
    print "fail request %s" % myreq.error.count("0")  # 打印错误请求数
    return avTime, myreq.error