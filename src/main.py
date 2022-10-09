from asyncio import InvalidStateError
from inspect import signature
from linebot import (LineBotApi,WebhookHandler)
from linebot.exceptions import InvalidSignatureError
from linebot.models import ( RichMenu, RichMenuArea,RichMenuSize,RichMenuBounds,PostbackEvent,MessageEvent,TextMessage,TextSendMessage)
from linebot.models.actions import (PostbackAction)
from flask import Flask, request, abort
from postback_action_manager import weather_action

# import configparser
# config_ini = configparser.ConfigParser()
# config_ini.read('./config.ini',encoding='utf=8')
# secret_key = config_ini['LineAPI']['channel_token']
# channel_secret = config_ini['LineAPI']['channel_secret']
secret_key = "5/zq9yuD6VLOd8zxTcI/aI4z2URKONA0tggDGU9yjBdZRKqAQfu+DcO/cpptHweOUMXs05qXqE23SKyzPgS1+6Su5Sn3WyF6pMmGXwXDld/err+ofEwxeL/eNOXwhojSNcw3WhA7XW1wd1k0hc9yXgdB04t89/1O/w1cDnyilFU="
channel_secret = "fafb23966c549ef943444db51ae9baa5"

linebot_api = LineBotApi(secret_key)
handler = WebhookHandler(channel_secret)

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello wold'
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(PostbackEvent)
def on_PostBack(event):
    postback_data = event.postback.data
    if postback_data == 'renew':
        #一番左側
        print('left')
    elif postback_data == 'deadline':
        #左側
        print('left1')
    elif postback_data == 'not_submitted':
        print('right')
    elif postback_data == 'forget':
        print('right1')
    else:
        print('else')
    

    linebot_api.reply_message(
        event.reply_token,
        TextSendMessage(text = "Postbackからです")
    )

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    linebot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="テスト中" )
    )
if __name__ == "__main__":
    # weather_action()
    app.run()