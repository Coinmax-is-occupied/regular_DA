import time
from apscheduler.schedulers.blocking import BlockingScheduler


def to_do():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


sched = BlockingScheduler()
sched.add_job(to_do, 'interval', days = 1)
sched.start()