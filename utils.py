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
    

def send_button_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":text,
                    "buttons":[
                        {
                            "type":"web_url",
                            "url":"https://www.facebook.com/2014%E6%96%B0%E6%98%A5%E6%85%88%E5%96%84%E7%89%B9%E6%BC%94-%E4%BB%8A%E5%A4%9C%E6%98%A5%E5%86%8D%E7%8F%BE-1374609219464670/",
                            "title":"2014新春慈善特演-\r\n今夜春再現"
                        },
                        {
                            "type":"web_url",
                            "url":"https://www.facebook.com/2015%E5%B1%8F%E4%B8%AD%E5%B1%8F%E5%A5%B3%E8%81%AF%E5%90%88%E6%88%B2%E5%8A%87%E5%85%AC%E6%BC%94%E5%9C%98%E5%8A%87-645400782261016/",
                            "title":"2015屏中屏女聯合戲劇公演-\r\n團劇"
                        },
                        {
                            "type":"web_url",
                            "url":"https://www.facebook.com/%E5%B1%8F%E6%9D%B1%E5%A5%B3%E4%B8%AD%E8%92%B2%E5%85%AC%E8%8B%B1%E5%8A%87%E5%9D%8A-283123625125577/",
                            "title":"屏東女中蒲公英劇坊"
                        }
                    ]
                }
            }
        }
    
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response
