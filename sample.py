import requests
requests.post('')

payload  = {
    'action':'add_course',
    #注意，json就是字符串，是一种特殊格式的字符串，还要注意跨行字符串
    'data':'''
    {
        "name":"初中化学",
        "dese":"初中化学教程",
        "display_idx":"4"
    }
    '''
}

