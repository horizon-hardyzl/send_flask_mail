#encoding:utf-8
from flask import Flask,render_template
from flask_mail import Mail,Message
import config
import os
path = os.path.dirname(__file__)
filename = os.path.join(path,'zlktqa.zip')

mail = Mail()

app = Flask(__name__)
app.config.from_object(config)

mail.init_app(app)

#发送文本
@app.route('/email_send_charactor/')
def email_send_charactor():
    message = Message(subject='hello flask-mail',recipients=['1052503676@qq.com'],body='flask-mail测试代码')
    try:
        mail.send(message)
        return '发送成功，请注意查收~'
    except Exception as e:
        print(e)
        return '发送失败'


#发送附带附件的邮件
@app.route('/email_send_attach/')
def email_send_attach():
    message = Message(subject='hello flask-mail',recipients=['1052503676@qq.com'],body='我是一个附件邮件')
    try:
        # message.attach邮件附件添加
        # 方法attach(self,
        #        filename=None,
        #        content_type=None,
        #        data=None,
        #        disposition=None,
        #        headers=None):

        with open(filename,'rb') as fp:
            message.attach("zlktqa.zip", "zip/zip", fp.read())
        mail.send(message)
        return '发送成功，请注意查收~'
    except Exception as e:
        print(e)
        return '发送失败'


if __name__ == '__main__':
    app.run()
