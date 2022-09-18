from asyncio import InvalidStateError
from inspect import signature
from linebot import (LineBotApi,WebhookHandler)
from linebot.exceptions import InvalidSignatureError
from linebot.models import ( RichMenu, RichMenuArea,RichMenuSize,RichMenuBounds,PostbackEvent,MessageEvent,TextMessage,TextSendMessage)
from linebot.models.actions import (PostbackAction)
from flask import Flask, request, abort

import configparser
config_ini = configparser.ConfigParser()
config_ini.read('./config.ini',encoding='utf=8')
secret_key = config_ini['LineAPI']['channel_token']
channel_secret = config_ini['LineAPI']['channel_secret']

linebot_api = LineBotApi(secret_key)
handler = WebhookHandler(channel_secret)

app = Flask(__name__)

# rich_menu_to_create = RichMenu(
#     size=RichMenuSize(width=2500, height=1686),
#     selected=True,
#     name='test_rich_menu',
#     chat_bar_text='メニュー',
#     areas=[
#         RichMenuArea(
#             bounds=RichMenuBounds(x=0,y=0,width=1273,height=868),
#             action=PostbackAction(data='renew',text="sample")
#         ),
#         RichMenuArea(
#             bounds=RichMenuBounds(x=1278,y=0,width=1211,height=864),
#             action=PostbackAction(data='deadline')
#         ),
#         RichMenuArea(
#             bounds=RichMenuBounds(x=0,y=864,width=1268,height=818),
#             action=PostbackAction(data='not_submitted')
#         ),
#         RichMenuArea(
#             bounds=RichMenuBounds(x=1273,y=877,width=1227,height=805),
#             action=PostbackAction(data='forget')
#         ),
#     ]
# )

# richMenuId = linebot_api.create_rich_menu(rich_menu=rich_menu_to_create)


# with open("richmenu1.png",'rb') as f:
#     linebot_api.set_rich_menu_image(richMenuId, "image/png",f)

# linebot_api.set_default_rich_menu(richMenuId)
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
    msg = event.postback.data
    txt = event.postback.text
    print(msg)
    print(txt)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    linebot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text )
    )
if __name__ == "__main__":
    app.run()