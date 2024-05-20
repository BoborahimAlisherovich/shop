import requests

def send_message(text):
    url = f"https://api.telegram.org/bot6705729790:AAGfYghjIzmTNu5_bUkDeogvaC0Aw08fjbg/sendMessage"
    params = {"chat_id": '1776373061', "text": text}
    response = requests.post(url, data=params)
    return response.json()