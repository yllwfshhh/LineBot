import os
import random

from linebot import LineBotApi, WebhookParser
from linebot.models import *

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(str(channel_access_token))

#music list
## each option 3 songs
music = ['https://open.spotify.com/track/3bC1ahPIYt1btJzSSEyyrF?si=72bb44eca92643be',
'https://open.spotify.com/track/6KgBpzTuTRPebChN0VTyzV?si=2a07ad61a4184087',
'https://open.spotify.com/track/0cqRj7pUJDkTCEsJkx8snD?si=4e510a7cbccb4a3c',
'https://open.spotify.com/track/4JiP9YjPXjP8Axcx779PKk?si=ca926b0000974fac',
'https://open.spotify.com/track/49AQAXswd32dFJUWOegVWO?si=04009bdb27a14111',
'https://open.spotify.com/track/39HrUxcvKF3jtLz7fUDWXc?si=18f68d98a62a401f',
'https://open.spotify.com/track/300Thm9XVWrKY0GlXhmGrz?si=863cedf27b234a52',
'https://open.spotify.com/track/7iYdGuVLqb5bwOlgA6oKGs?si=03aa52cd2f214313',
'https://open.spotify.com/album/6zRvJSG5JLRAQ2YAmP8R1a']

#sticker list
## each option 3 stickers
## last 2 stickers for [goodnigt] and [goodbye]
sticker = [ 11538,51626501,11538,51626503,8525,16581300, 1070,17842,11538,51626494,11539,52114122,  8515,16581247,446,1989,11538,51626495,11538,51626513,8515,16581253]

#string list
## each option 3 strings
music_str = ["Keep it on BABE!",
"贊贊的繼續保持喵",
"你超棒的喵喵",
"Then let this song make your day",
"喵喵喵",
"要期末考了喵",
"It's okay to be NOT okay sometimes , you have tried your best .",
"I know this won’t be easy, but I also know you’ve got the strength to get through.",
"I’m here with you all the time meow~"]
# .

#meme
## each option 5 pics
meme =['https://remote-tools-images.s3.amazonaws.com/programmer-memes/14.jpg',
'https://preview.redd.it/bwg5l8hsafr71.jpg?auto=webp&s=83e6522bedb7aaba5754891e232320661dc8e4ec',
'https://gitpiper.com/assets/memes/programming-meme-ff7166d5-d272-4fce-8e30-cef42a514420.webp',
'https://i.pinimg.com/564x/3b/d6/cb/3bd6cb9e6996247800e393a208367597.jpg',
'https://i.pinimg.com/564x/b3/2e/8e/b32e8eea5d525dacdada5c3ae97a0bdb.jpg',
'https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/320419572_5216092508495531_3000110373889080804_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=y3CidK0HEq4AX9aQ2pG&_nc_ht=scontent-tpe1-1.xx&oh=00_AfAikqqplHdTauJ6KouRmTVI9V3nLTADLZIe8NbAkL7ToA&oe=63AA5B23',
'https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/318658024_649242663604579_2908051439536781118_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=5cd70e&_nc_ohc=4jhztOFKfNEAX95JmYu&_nc_ht=scontent-tpe1-1.xx&oh=00_AfDpWlcWRUGGbyH_eb55BwAo1FpgH7wuM5q-8nu_XDnzuw&oe=63A9BB8E',
'https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/318117510_3403442436580188_5863779501879882588_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=5cd70e&_nc_ohc=7NLaT4KiOjgAX-46Leb&_nc_ht=scontent-tpe1-1.xx&oh=00_AfBNKFw_p4w1ImGme9KwWjANzltwnhQKXKXoKoFeAfklrg&oe=63A97E68',
'https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/316818632_673521277671814_917635173606214014_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=6fhjAmknSnEAX8GeD__&tn=WGlLjI7D5WzmY-vz&_nc_ht=scontent-tpe1-1.xx&oh=00_AfAZA6nvNbbr58Pp-AIs_zHG62R3jJj3Iu0_Dq6EgIGnRg&oe=63A98F05',
'https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/315092065_460169886239408_5246701327433955831_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=5cd70e&_nc_ohc=aVKp_6p48a0AX9F2bXJ&tn=WGlLjI7D5WzmY-vz&_nc_ht=scontent-tpe1-1.xx&oh=00_AfApb5FxG_MkE4ybcr-O5IpNrnBxwXJXfQ9AF1KAUhEZbA&oe=63AA5FD1']

#template
ask_template = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            title='What kind of service you want today ? ',
            text="( Φ ω Φ )",
            thumbnail_image_url='https://scontent.xx.fbcdn.net/v/t1.15752-9/317814062_2680767402065205_5699598980573016567_n.jpg?stp=dst-jpg_p173x172&_nc_cat=107&ccb=1-7&_nc_sid=aee45a&_nc_ohc=chi_YN6NI5MAX-q1wVP&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdTANYPk250XGj23X07i3wSGkueD7_TqhViWj7CR4wttKA&oe=63C172AC',
            image_aspect_ratio="square",
            actions=[
                MessageTemplateAction(
                    label='Music',
                    text='Any music recommendations?'
                ),
                MessageTemplateAction(
                    label='Meme',
                    text='meme'
                ),
                URITemplateAction(
                    label='Mini Game',
                    uri='https://poki.com/en/g/where-is-my-cat'
                )  
            ]
        )
    )         

music_template = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='How is your mood ? ',
                text="( Φ ω Φ )",
                thumbnail_image_url='https://i.ytimg.com/vi/7xC0Rqw9yTA/maxresdefault.jpg',
                image_aspect_ratio="square",
                actions=[
                    MessageTemplateAction(
                        label='Good',
                        text='I feel good today!'
                    ),
                    MessageTemplateAction(
                        label='Normal',
                        text='Nothing special today~'
                    ),
                    MessageTemplateAction(
                        label='Bad',
                        text="I'm not in a good mood right now..."
                    ),
                ]
            )
        )         

confirm_template = TemplateSendMessage(
        alt_text='Confirm template',
        template=ConfirmTemplate(
            title='Are you a programmer?',
            text='Are you a programmer?',
            actions=[                              
                MessageTemplateAction(
                    label='Yes',
                    text='Yes'
                ),
                MessageTemplateAction(
                    label='No',
                    text='No'
                )
            ]
        )
    )
        
def send_text_message(reply_token ,text):
    # line_bot_api.push_message(id, TextSendMessage(text=text))
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

def reply_music(reply_token,mode):
    
    if mode=='good':
        id = random.randrange(0,5,2)
        msg = music_str[random.randint(0,2)] + "\n\U00002728%s\U00002728" %music[random.randint(0,2)]
    elif mode=='normal':
        id = random.randrange(6,11,2)
        msg = music_str[random.randint(3,5)] + "\n\U00002728%s\U00002728" %music[random.randint(3,5)]
    elif mode=="bad":
        id = random.randrange(12,17,2)
        msg = music_str[random.randint(6,8)] + "\n\U00002728%s\U00002728" %music[random.randint(6,8)]

    line_bot_api.reply_message(reply_token, [
        TextSendMessage(text= msg),
        StickerSendMessage( package_id = sticker[id] ,sticker_id = sticker[id+1])
        ])

def reply_exit(reply_token,mode):
    
    msg = "error"
    id = 0
    if mode==1:
        id = 18
        msg = "Good night~ Have a sweet dream my babe \U0001F319"
    elif mode==2:
        id = 20
        msg = "Bye see you next time!"

    line_bot_api.reply_message(reply_token, [
        TextSendMessage(text= msg),
        StickerSendMessage( package_id = sticker[id] ,sticker_id = sticker[id+1])
        ])

def send_video(reply_token):
    video_url = 'https://imgur.com/a/tBHUrWC'
    line_bot_api.reply_message(reply_token,VideoSendMessage(original_content_url=video_url,preview_image_url=video_url))

    
def send_img(reply_token,state):
    if state == "yes":
        img_url = meme[random.randint(0, 4)]
    if state == "no" : 
        img_url = meme[random.randint(5, 9)]
    line_bot_api.reply_message(reply_token,ImageSendMessage(original_content_url=img_url,preview_image_url=img_url))

def send_template(reply_token):
    line_bot_api.reply_message(reply_token, ask_message)

    

