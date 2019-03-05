import telegram
bot = telegram.Bot(token='637785666:AAHRW-gz-CeKkSGbP_xKubcau0dO28ffBYc')
print bot.getMe()
bot.send_message('FindSthToPlay',
    '<a href="http://cn.bing.com">bing</a>.', 
    parse_mode=telegram.ParseMode.HTML)
