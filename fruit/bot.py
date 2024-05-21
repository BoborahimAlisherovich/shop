import requests

def send_message(text):
    url = f"https://api.telegram.org/bot7150380677:AAHOQ-WwfPN1Xd-W4_-KOhLXJPT0aWLgh0M/sendMessage"
    params = {"chat_id": '6208545740', "text": text}
    response = requests.post(url, data=params)
    return response.json()