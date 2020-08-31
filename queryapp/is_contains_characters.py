#conding=utf-8
class IsContainsCharacters(object):
    '''检查是否含有关键字'''
    def __init__(self, keyword):
        self.keyword = keyword
        self.characters = [';','"']
        self.hosts = "No hosts matched"

    def get_ret(self):
        tag = 0
        for character in self.characters:
            if character in self.keyword:
                tag+=1
            else:
                tag=tag
        return tag

    def get_hosts(self):
        '''判断ansible hosts是否有改组件配置'''
        tag = 0
        if self.hosts in self.keyword:
            tag += 1
        return tag
# bb = "dsfadf"
# aa = IsContainsCharacters(bb)
# print(aa.get_ret())