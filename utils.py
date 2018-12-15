import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAFClPHBVGYBAAvZAqJDCZCwWZBrH6PJqITdy7BfgL8gq9crgEeGrRmtpfBPVzd7ORHQ1nfJvZBZBjZCQrAb3osU0IPfNfEhyZBBiLX7HlsNqspBCPbPt5otq75ls76hUY9u1s2lB7vDq3l0Qzp7wOYokU7Ub3etd10enEozkr3Uf90mIaljlg2"


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
