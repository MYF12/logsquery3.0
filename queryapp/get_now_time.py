import time
class GetNowTime(object):
    def __init__(self):
        self.nowtime = str(time.strftime('%y%m%d%H%M%S',time.localtime(time.time())))
    def getNowTime(self):
        return self.nowtime
