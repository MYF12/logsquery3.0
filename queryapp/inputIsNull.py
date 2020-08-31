#conding = utf-8

def input_is_null(key_tmp):
    '''
    判断用户输入是否为空
    为空：return 0
    不为空：return 1
    '''
    key_tmp = key_tmp
    if  key_tmp:
        return 1
    else:
        result_content = "%s 不能输出为空！"
        context = {'result_content': result_content}
        print(1)
        return context
key_tmp=''
input_is_null(key_tmp)
