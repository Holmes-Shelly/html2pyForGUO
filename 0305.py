import requests
TOKEN = "637785666:AAHRW-gz-CeKkSGbP_xKubcau0dO28ffBYc"
url = "https://api.telegram.org/bot{}/".format(TOKEN)
# print requests.get(url +"getme").content
# print requests.get(url + "getUpdates").content
def send_message(msg):
	status = requests.get(url + "sendMessage?chat_id=-1001366507371&text={}".format(msg)).content
	return status
print send_message("8 updated, 2 important")
