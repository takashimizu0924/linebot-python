from linebot.models import ( RichMenu, RichMenuArea,RichMenuSize,RichMenuBounds,PostbackEvent,MessageEvent,TextMessage,TextSendMessage)
from linebot.models.actions import (PostbackAction)


rich_menu_to_create = RichMenu(
    size=RichMenuSize(width=2500, height=1686),
    selected=True,
    name='test_rich_menu',
    chat_bar_text='メニュー',
    areas=[
        RichMenuArea(
            bounds=RichMenuBounds(x=0,y=0,width=1273,height=868),
            action=PostbackAction(data='renew',text="sample")
        ),
        RichMenuArea(
            bounds=RichMenuBounds(x=1278,y=0,width=1211,height=864),
            action=PostbackAction(data='deadline')
        ),
        RichMenuArea(
            bounds=RichMenuBounds(x=0,y=864,width=1268,height=818),
            action=PostbackAction(data='not_submitted')
        ),
        RichMenuArea(
            bounds=RichMenuBounds(x=1273,y=877,width=1227,height=805),
            action=PostbackAction(data='forget')
        ),
    ]
)

# richMenuId = linebot_api.create_rich_menu(rich_menu=rich_menu_to_create)


# with open("richmenu1.png",'rb') as f:
#     linebot_api.set_rich_menu_image(richMenuId, "image/png",f)

# linebot_api.set_default_rich_menu(richMenuId)