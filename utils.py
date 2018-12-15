import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAFClPHBVGYBANH9YTL9owvHMyP1f25ruZCeiVhny4eqoZBUZA2F8ZAB8nFZBg5W8FZB2qT8ap0w5ecBiXg5uIFsy0HJsh6fP9fFIceMLh3gqH3GjqLnhHZAs3RASo8m426OoWxBGhobDDGwkZACGHJ8qyRFPZAkSjZA5ih2Ownv1hZB9tRI2oK6cGE"


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
