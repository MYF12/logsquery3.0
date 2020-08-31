#conding = utf-8
import os
from django.conf import settings
from django.http import StreamingHttpResponse
from django.shortcuts import render
from .logcheck import ZuJianLogs
from . import inputIsNull
from .logs_new_content import LogsNewContent
from .get_file_num import GetFileNum
from .ls_logs_format import IsLogsFormat



def index(request):
    return render(request,'queryapp/index.html')
def query1(request):
    return render(request, 'queryapp/query1.html')

def queryresult1(request):
    '''查看当前日志最新日志'''
    zjname = request.POST['zjname']
    keywords = request.POST['keywords']
    logsfile_tmp = request.POST['logsfile']
    logsfile = logsfile_tmp
    hnum = request.POST['hnum']
    tailhnum = request.POST['tailhnum']
    if hnum:
        hnum = hnum
    else:
        hnum = 0
    if tailhnum:
        tailhnum = tailhnum
    else:
        tailhnum = 5000

    log_check = ZuJianLogs()
    result_file = log_check.grep(zjname, keywords, logsfile, hnum,tailhnum)
    logs_file = log_check.logs_file
    # 获取文件名，用于下载
    split_lists = logs_file.split('/')
    lists_count = len(split_lists)
    filename = split_lists[lists_count-1]
    #获取文件行数
    file_count = log_check.get_file_num(logs_file)
    if file_count <= 5000:
        try:
            with open(logs_file, "r", encoding='utf-8') as f:
                # result_content = f.read()
                result_content = f.readlines()

        except:
            result_content = "文件不存在"
        context = {'zjname': zjname,
                   'keywords':keywords,
                   'logsfile':logsfile,
                   'result_content':result_content,
                   'hnum': hnum,
                   "logs_file_name": filename,
                   'tailhnum': tailhnum
                   }
    else:
        context = {'zjname': zjname,
                   'keywords':keywords,
                   'logsfile':logsfile,
                   'result_content':"文件输出太大，请下载查看！",
                   "file_count":file_count,
                   "logs_file_name": filename
                   }
    return render(request, 'queryapp/query1.html', context)



def downfile(request):
    filename = request.GET['filename']
    filepath = os.path.join(os.getcwd()+"/queryapp/static/files/"+filename)
    fp = open(filepath, 'rb')
    response = StreamingHttpResponse(fp)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="%s"' %filename.encode('utf-8').decode('ISO-8859-1')
    return response



def logsnewcontent(request):
    return render(request, 'queryapp/logsnewcontent.html')
def logsnewcontent1(request):
    '''
    查询组件最新日志
    '''
    zjname = request.POST['zjname']
    logsfile = request.POST['logsfile']
    tailhnum = request.POST['tailhnum']
    tailhnum = isNull(tailhnum, 10)

    logs_check = LogsNewContent(zjname, logsfile, tailhnum)
    result_file = logs_check.tail_cmd()
    # 获取文件名，用于下载
    split_lists = result_file.split('/')
    lists_count = len(split_lists)
    filename = split_lists[lists_count - 1]
    # 获取文件行数
    count_obj = GetFileNum(result_file)
    file_count = count_obj.getFileNum()

    if file_count <= 5000:
        try:
            with open(result_file, "r", encoding='utf-8') as f:
                # result_content = f.read()
                result_content = f.readlines()
        except:
            result_content = "文件不存在"
        context = {'zjname': zjname,
                   'logsfile':logsfile,
                   'tailhnum': tailhnum,
                   "logs_file_name": filename,
                   'result_content': result_content,
                   }
    else:
        context = {'zjname': zjname,
                   'logsfile':logsfile,
                   'tailhnum': tailhnum,
                   "logs_file_name": filename,
                   'result_content': "文件输出太大，请下载查看！"
                   }
    return render(request, 'queryapp/logsnewcontent.html', context)

def logsformat(request):
    return render(request, 'queryapp/logsformat.html')
def logsformatForm(request):
    zjname = request.POST['zjname']
    logsfile = request.POST['logsfile']
    logs_check = IsLogsFormat(zjname, logsfile)
    result_file = logs_check.ls_cmd()
    # 获取文件名，用于下载
    split_lists = result_file.split('/')
    lists_count = len(split_lists)
    filename = split_lists[lists_count - 1]
    with open(result_file, "r", encoding='utf-8') as f:
        # result_content = f.read()
        result_content = f.readlines()
    context = {'zjname': zjname,
               'logsfile':logsfile,
               "logs_file_name": filename,
               'result_content': result_content,
               }
    return render(request, 'queryapp/logsformat.html', context)


def isNull(param, reparam):
    '''判断用户是否正常输入，是则返回用户输入，否则返回默认值'''
    if param:
        return param
    else:
        return reparam










