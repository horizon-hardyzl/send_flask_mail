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




if __name__ == '__main__':
    app.run()
