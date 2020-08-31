#conding=utf-8
import  subprocess
import os,sys, time
from .is_contains_characters import IsContainsCharacters
from .write_file import WirteFile

class LogsNewContent(object):
    '''查询组件最新日志输出'''
    def __init__(self, zjname, logsfile, tailhnum):
        self.nowtime = str(time.strftime('%y%m%d%H%M%S', time.localtime(time.time())))
        self.zjname = zjname
        self.logsfile = logsfile
        self.tailhnum = tailhnum
        self.filename =  zjname.replace(" ", "")+"_%s.txt"%(self.nowtime)
        self.logs_file = os.path.join(os.getcwd()+"/queryapp/static/files/"+self.filename)



    def tail_cmd(self):
        # judgeChara = IsContainsCharacters(self.zjname)
        if IsContainsCharacters(self.zjname).get_ret() == 0 \
                and IsContainsCharacters(self.logsfile).get_ret() == 0 :
            tailCmd = "ansible %s --sudo -m shell -a \" tail -%s %s\" "\
                      %(self.zjname, self.tailhnum, self.logsfile)
            # content = '测试'
            cmd_retcode, cmd_output = subprocess.getstatusoutput(tailCmd)
            if len(cmd_output) < 300 and IsContainsCharacters(cmd_output).get_hosts() == 1:
                wirte_file = WirteFile(self.logs_file, "ansible 配置没有该组件，请联系运维添加到/etc/ansible/hosts文件中！")
                wirte_file.get_results_file()
            else:
                wirte_file = WirteFile(self.logs_file, cmd_output)
                wirte_file.get_results_file()
        else:
            content = '组件或者日志路径不允许输入 " 号和 ; 号'
            wirte_file = WirteFile(self.logs_file, content)
            wirte_file.get_results_file()
        return self.logs_file




# zjname = 'mtsmsgw'
# judgeChara = IsContainsCharacters(zjname)
# print(IsContainsCharacters(zjname).get_ret())