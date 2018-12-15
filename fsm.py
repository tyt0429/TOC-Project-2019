from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state_session(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '查詢演出場次'
        return False

    def is_going_to_state_ticket_prcie(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '查詢票價'
        return False

    def is_going_to_state_sponsor(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '我想贊助你們'
        return False

    def is_going_to_state_Jan(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '一月'
        return False

    def is_going_to_state_Feb(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '二月'
        return False

    def is_going_to_state_March(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '三月'
        return False

    def is_going_to_state_price1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '貴賓席'
        return False

    def is_going_to_state_price2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '搖滾區'
        return False

    def is_going_to_state_price3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '一般區'
        return False

    def is_going_to_state_buy(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '確認購買'
        return False

    def is_going_to_state_transfer(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '是'
        return False

    def is_going_to_state_sponsor1000(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '$1000'
        return False

    def is_going_to_state_sponsor5000(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '$5000'
        return False

    def is_going_to_state_sponsor10000(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '$10000'
        return False

    def is_going_to_state_crew_list(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '查詢工作人員名單'
        return False

    def is_going_to_state_detail_info(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '場次詳細資訊'
        return False

    def on_enter_state_session(self, event):
        print("I'm entering state_session")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "您想要查詢哪一個月份的場次?(一月/二月/三月)")

    def on_exit_state_session(self, event):
        print('Leaving state_session')

    def on_enter_state_ticket_prcie(self, event):
        print("I'm entering state_ticket_prcie")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "您想查詢什麼位置的票價?(貴賓席/搖滾區/一般區)")

    def on_exit_state_ticket_prcie(self, event):
        print('Leaving state_ticket_prcie')
        
    def on_enter_state_sponsor(self, event):
        print("I'm entering state_sponsor")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "使用轉帳(是)")

    def on_exit_state_sponsor(self, event):
        print('Leaving state_sponsor')
        
    def on_enter_state_transfer(self, event):
        print("I'm entering state_transfer")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "請輸入贊助金額($1000/$5000/$10000)")

    def on_exit_state_transfer(self, event):
        print('Leaving state_transfer')
        
    def on_enter_state_Jan(self, event):
        print("I'm entering state_Jan")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "一月演出場次為1/11(五) 1/18(五) 1/25(五)\n輸入'場次詳細資訊'以獲得更多資訊")

    def on_exit_state_Jan(self, event):
        print('Leaving state_Jan')
        
    def on_enter_state_Feb(self, event):
        print("I'm entering state_Feb")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "二月演出場次為2/15(五) 2/22(五)\n輸入'場次詳細資訊'以獲得更多資訊")

    def on_exit_state_Feb(self, event):
        print('Leaving state_Feb')
        
    def on_enter_state_March(self, event):
        print("I'm entering state_March")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "三月演出場次為3/04(五) 3/11(五)\n輸入'場次詳細資訊'以獲得更多資訊")

    def on_exit_state_March(self, event):
        print('Leaving state_March')
        
    def on_enter_state_price1(self, event):
        print("I'm entering state_price1")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "貴賓席的票價為$800\n是否確認購買(確認購買)")

    def on_exit_state_price1(self, event):
        print('Leaving state_price1')
        
    def on_enter_state_price2(self, event):
        print("I'm entering state_price2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "搖滾區的票價為$500\n是否確認購買(確認購買)")

    def on_exit_state_price2(self, event):
        print('Leaving state_price2')
        
    def on_enter_state_price3(self, event):
        print("I'm entering state_price3")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "一般區的票價為$300\n是否確認購買(確認購買)")

    def on_exit_state_price3(self, event):
        print('Leaving state_price3')
        
    def on_enter_state_buy(self, event):
        print("I'm entering state_buy")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "購買成功!!!感謝您的支持~")
        self.go_back()

    def on_exit_state_buy(self):
        print('Leaving state_buy')
        
    def on_enter_state_sponsor1000(self, event):
        print("I'm entering state_sponsor1000")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "謝謝您贊助我們1000^^")
        self.go_back()

    def on_exit_state_sponsor1000(self):
        print('Leaving state_sponsor1000')
        
    def on_enter_state_sponsor5000(self, event):
        print("I'm entering state_sponsor5000")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "謝謝您贊助我們5000^^")
        self.go_back()

    def on_exit_state_sponsor5000(self):
        print('Leaving state_sponsor5000')
        
    def on_enter_state_sponsor10000(self, event):
        print("I'm entering state_sponsor10000")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "非常感謝您贊助我們10000^^")
        self.go_back()

    def on_exit_state_sponsor10000(self):
        print('Leaving state_sponsor10000')
        
    def on_enter_state_crew_list(self, event):
        print("I'm entering state_crew_list")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "工作人員名單如下\n------藝術組------\n導演：湯雅瑭\n編劇：吳念真\n演員：陳怡亘 吳念真 郭予凡\n陳宜青 張瑋庭 徐子歡\n\n------技術組------\n舞台監督：黃臆璇\n舞台設計：馬佳琳\n舞台組員：蔡欣芸 張碩真 藍詩雅 林欣融\n燈光設計：李沛思\n音效設計：王凱莉\n服化妝設計：黃子菁\n服化妝組員：吳念真 吳沛潔\n\n------行政組------\n行政組長：曾恩瑜\n宣傳：馬佳琳 何竹昀 張碩真\n公關：黃沛瑀 藍詩雅\n前台：秦仕真 吳欣凌 蔡欣芸 林欣融 黃珮慈")
        self.go_back()

    def on_exit_state_crew_list(self):
        print('Leaving state_crew_list')
        
    def on_enter_state_detail_info(self, event):
        print("I'm entering state_detail_info")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "該月場次資訊:\n\n地點\n屏東藝術館(中正藝術館)\n900屏東縣屏東市和平路427號\n\n時間:\n18:00入場\n18:30開演")
        self.go_back()

    def on_exit_state_detail_info(self):
        print('Leaving state_detail_info')
