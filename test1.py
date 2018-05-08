import re
question = input('那么先告诉你的名字吧：')
answer = {question:'你好，%s' % question}
def train():
    global question
    global answer
    while answer:
        if answer.get(question):
            print((answer.get(question)))
            question = input('你有什么问题呢？')
        else:
            var = input('抱歉，我不知道怎么做，能告诉我吗？')
            answer[question]=var
            var = input('那么现在，重新来提问我吧！')
train()
