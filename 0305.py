import telegram
bot = telegram.Bot(token='637785666:AAHRW-gz-CeKkSGbP_xKubcau0dO28ffBYc')
print bot.getMe()
bot.send_message(chat_id='FindSthToEat', text="msg test from s.h")
