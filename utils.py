import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAFClPHBVGYBANTUliug7YgE1EFBZC235GZCfBVP11X37JNTALu4lSUbv4vPlZAnvM4hkZAm6l4ZARHpnctxRZBOspI1Q2W9sPJUs3vtNPn2ZCLBL8KYQ4GhnnP2UXS57ETINZAIVq5DnGoZBM9Fkzsrq1oKCyzMPtq6Niku9m6rZAm8GRoAvzqDtp"


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



def send_image_url(id, img_url):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {
			"attachment":{
				"type":"image",
				"payload":{
					"url":img_url,
					"is_reusable":True
			}
		}
    }
	}
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response
    

def send_button_message(id, text, buttons):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":"What do you want to do next?",
                    "buttons":[
                        {
                            "type":"web_url",
                            "url":"https://www.messenger.com",
                            "title":"Visit Messenger"
                        },
                        {
                            "type":"web_url",
                            "url":"https://www.messenger.com",
                            "title":"Visit Messenger"
                        },
                    ]
                }
            }
        }
    
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response
