from transitions.extensions import GraphMachine
from utils import *



class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    
    def is_ask(self, event):
        text = event.message.text
        if "hi" or "hello"  in text.lower:    
            flag = 1    
        return flag

    def on_enter_ask(self, event):
        line_bot_api.reply_message(event.reply_token, ask_template)
        
    def is_music(self,event):
        text = event.message.text
        return text == "Any music recommendations?"

    def on_enter_music(self, event):
        line_bot_api.reply_message(event.reply_token, music_template)
               
    def is_good(self, event):
        text = event.message.text
        return text == "I feel good today!"

    def on_enter_good(self, event):    
        reply_music(event.reply_token,"good")
       

    def is_normal(self, event):
        text = event.message.text
        return text == "Nothing special today~"

    def on_enter_normal(self, event):
        reply_music(event.reply_token,"normal")
       

    def is_bad(self, event):
        text = event.message.text
        return text == "I'm not in a good mood right now..."

    def on_enter_bad(self, event):
        reply_music(event.reply_token,"bad")
       
    
    def is_meme(self, event):
        text = event.message.text
        return text.lower() == "meme"

    def on_enter_meme(self, event):
        line_bot_api.reply_message(event.reply_token,confirm_template)
 
    def is_yes(self, event):
        text = event.message.text
        return text.lower() == "yes"

    def on_enter_yes(self, event):
        send_img(event.reply_token,"yes")
      
    def is_no(self, event):
        text = event.message.text
        return text.lower() == "no"

    def on_enter_no(self, event):
        send_img(event.reply_token,"no")

    def is_replay(self, event):
        text = event.message.text
        return text == "ok"

    def is_exit(self, event):
        flag = 0
        text = event.message.text
        if text == "bye" or text=="goodnight" :
            flag = 1
        print(flag)
        return flag

    def on_enter_exit(self, event):
        exit_mode=2
        text = event.message.text
        if "night" in text.lower():
            exit_mode=1
        reply_exit(event.reply_token,exit_mode)
        self.go_back()
      


    
        
    