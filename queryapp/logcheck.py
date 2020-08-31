#conding=utf-8
import  subprocess
import os,sys, time
# sys.path.append("../")
# from logsquery import settings
from django.conf import settings
from .is_contains_characters import IsContainsCharacters
# 导入time模块
# import time
# # 打印时间戳
# print(time.time())
from .write_file import WirteFile
import re


class ZuJianLogs(object):
    ANSIBLE_HOSTS="/etc/ansible/hosts"
    # STATIC_FILES = os.path.join(settings.STATIC_ROOT+"/files")
    def __init__(self):
        self.nowtime = str(time.strftime('%y%m%d%H%M%S', time.localtime(time.time())))

    def grep(self,zjname,keywords,logsfile, hnum, tailhnum):
        '''
        grep 日志查询
        :param zjname:组件名称
        :param keywords: 关键字
        :param logsfile: 日志名称
        :return: 文件路径
        '''
        #获取关键字第一个因为，看下是不是命令，如果是的话则不执行操作

        cmd_tmp = keywords.strip().split()[0]
        self.check_cmd = "which" + " " + cmd_tmp
        self.retcode,self.output = subprocess.getstatusoutput(self.check_cmd)
        #self.ansible_tmp = "ansible %s --sudo -f 10 -m shell -a \"grep %s %s\" " % (zjname, keywords, logsfile)
        if self.retcode != 0:
            # self.ansible_cmd  = "ansible %s --sudo -f 10 -m shell -a \'grep \"%s\" /usr/local/vvm/%s  -C %s | tail -%s\' "\
            self.ansible_cmd = "ansible %s --sudo -f 10 -m shell -a \'grep \"%s\" %s  -C %s | tail -%s\' " \
                               %(zjname, keywords,logsfile, hnum, tailhnum)
            self.ansible_retcode, self.ansible_output = subprocess.getstatusoutput(self.ansible_cmd)
            #self.filename = keywords.replace(" ", "") + "_" + self.nowtime + ".txt"
            self.filename = re.sub(r'[/ :]*', '', keywords) + "_" + self.nowtime + ".txt"
            self.logs_file = os.path.join(os.getcwd()+"/queryapp/static/files/"+self.filename)
            if IsContainsCharacters(zjname).get_ret() != 0 \
                    or IsContainsCharacters(logsfile).get_ret() != 0:
                content = '组件或者日志路径不允许输入 " 号和 ; 号'
                wirte_file = WirteFile(self.logs_file, content)
                wirte_file.get_results_file()
                return self.logs_file

            self.write_file(self.ansible_output)
            # 判断是否存在改组件或者IP
            if len(self.ansible_output) < 300 and IsContainsCharacters(self.ansible_output).get_hosts() == 1:
                wirte_file = WirteFile(self.logs_file, "ansible 配置没有该组件，请联系运维添加到/etc/ansible/hosts文件中！")
                wirte_file.get_results_file()
                return self.logs_file

        else:
            self.logs_file = os.path.join(os.getcwd() + "/queryapp/static/files/" + self.nowtime + "_error.log")
            self.write_file(self.ansible_output)
            return self.logs_file

    def write_file(self,  file_content):
        self.file_content = file_content
        with open(self.logs_file, "w+", encoding="utf-8") as f:
            f.write(self.file_content + "\n")
        #print(self.logs_file)

    def get_file_num(self, filename):
        filename = filename
        count = 0
        for count, line in enumerate(open(filename, 'rU', encoding='utf-8')):
            count += 1
        return count

    def input_is_null(self, key_tmp, name_tmp):
        '''
        判断用户输入是否为空
        为空：return 文件名
        不为空：return True
        '''
        if key_tmp:
            return True
        else:
            self.logs_file = os.path.join(os.getcwd() + "/queryapp/static/files/"+self.nowtime+ "_error.log")
            self.write_file("%s不能为空"%(name_tmp))
            return self.logs_file

    def get_radon(self):
        return  self.ANSIBLE_HOSTS







# logs_check = ZuJianLogs()
# logs_check.grep("mtsms","哈哈","/data")
# # print(logs_check.retcode)
# print(logs_check.ansible_cmd)
# print(logs_check.ansible_output)
# # print(logs_check.grep("mtsms","haha","/data"))
# print(logs_check.logs_file)
# logs_check.write_file("111111")
#
#
# logs_check.grep("mtsms","hehe","/data", 10)
# print(logs_check.ansible_cmd)
# print(logs_check.logs_file)
# # logs_check.write_file("222222")


