import requests
token = "637785666:AAHRW-gz-CeKkSGbP_xKubcau0dO28ffBYc"
print requests.get("https://api.telegram.org/bot<token>/getme".replace("<token>", token))
url = "https://api.telegram.org/bot<token>/sendMessage?chat_id=@FindSthToEat&text=message"
print requests.get(url.replace("<token>", token))