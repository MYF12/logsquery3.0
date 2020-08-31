class WirteFile(object):
    '''用于写入内容到文件'''
    def __init__(self, filename, content):
        self.filename = filename
        self.content = content

    def get_results_file(self):
        '''输出内容写入文件，并返回文件路径'''
        with open(self.filename, "w+", encoding="utf-8") as f:
            f.write(self.content + "\n")
        # return self.filename
