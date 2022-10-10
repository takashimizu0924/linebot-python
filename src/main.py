from asyncio import InvalidStateError
from inspect import signature
from linebot import (LineBotApi,WebhookHandler)
from linebot.exceptions import InvalidSignatureError
from linebot.models import ( RichMenu, RichMenuArea,RichMenuSize,RichMenuBounds,PostbackEvent,MessageEvent,TextMessage,TextSendMessage,CarouselTemplate,CarouselColumn,ImageCarouselColumn,ImageCarouselTemplate,TemplateSendMessage)
from linebot.models.actions import (PostbackAction)
from flask import Flask, request, abort
# from postback_action_manager import weather_action
from .instagram import Instagram

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
    insta = Instagram()
    if postback_data == 'renew':
        #一番左側
        # print('left')
        # linebot_api.reply_message(
        # event.reply_token,
        # TextSendMessage(text = "renewです")
    # )
        columns_list = []
        media_list = insta.GetHashTagMain("豚肉レシピ")
        columns_list.append(ImageCarouselColumn(image_url=media_list[0]["mediaUrls"][0],action=PostbackAction(label='postback1',display_text='postback text1',data='action=buy&itemid=1')))
        columns_list.append(ImageCarouselColumn(image_url=media_list[1]["mediaUrls"][0],action=PostbackAction(label='postback1',display_text='postback text1',data='action=buy&itemid=1')))
        columns_list.append(ImageCarouselColumn(image_url=media_list[2]["mediaUrls"][0],action=PostbackAction(label='postback1',display_text='postback text1',data='action=buy&itemid=1')))
        columns_list.append(ImageCarouselColumn(image_url=media_list[3]["mediaUrls"][0],action=PostbackAction(label='postback1',display_text='postback text1',data='action=buy&itemid=1')))
        columns_list.append(ImageCarouselColumn(image_url=media_list[4]["mediaUrls"][0],action=PostbackAction(label='postback1',display_text='postback text1',data='action=buy&itemid=1')))
        
        image_carousel_template = TemplateSendMessage(alt_text='Image',template=ImageCarouselTemplate(columns=columns_list))
        linebot_api.reply_message(event.reply_token,messages=image_carousel_template)
        
    elif postback_data == 'deadline':
        #左側
        print('left1')
    elif postback_data == 'not_submitted':
        print('right')
    elif postback_data == 'forget':
        print('right1')
    else:
        print('else')
    

    # linebot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text = "Postbackからです")
    # )

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    linebot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="テスト中" )
    )
if __name__ == "__main__":
    # weather_action()
    app.run()