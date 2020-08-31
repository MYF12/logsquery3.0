class GetFileNum(object):
    def __init__(self, filename):
        self.filename = filename
    def getFileNum(self):
        count=0
        for count, line in enumerate(open(self.filename, 'rU',encoding='utf-8')):
            count+=1
        return count