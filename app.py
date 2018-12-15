from bottle import route, run, request, abort, static_file

from fsm import TocMachine


VERIFY_TOKEN = "F64044078"
machine = TocMachine(
    states=[
        'user',
        'state_session',
        'state_ticket_prcie',
		'state_sponsor',
		'state_transfer',
		'state_Jan',
		'state_Feb',
		'state_March',
		'state_price1',
		'state_price2',
		'state_price3',
		'state_buy',
		'state_sponsor1000',
		'state_sponsor5000',
		'state_sponsor10000',
		'state_crew_list',
		'state_detail_info'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state_session',
            'conditions': 'is_going_to_state_session'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state_ticket_prcie',
            'conditions': 'is_going_to_state_ticket_prcie'
        },
		{
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state_sponsor',
            'conditions': 'is_going_to_state_sponsor'
        },
		{
            'trigger': 'advance',
            'source': 'state_session',
            'dest': 'state_Jan',
            'conditions': 'is_going_to_state_Jan'
        },
		{
            'trigger': 'advance',
            'source': 'state_session',
            'dest': 'state_Feb',
            'conditions': 'is_going_to_state_Feb'
        },
		{
            'trigger': 'advance',
            'source': 'state_session',
            'dest': 'state_March',
            'conditions': 'is_going_to_state_March'
        },
		{
            'trigger': 'advance',
            'source': 'state_Jan',
            'dest': 'state_detail_info',
            'conditions': 'is_going_to_state_detail_info'
        },
		{
            'trigger': 'advance',
            'source': 'state_Feb',
            'dest': 'state_detail_info',
            'conditions': 'is_going_to_state_detail_info'
        },
		{
            'trigger': 'advance',
            'source': 'state_March',
            'dest': 'state_detail_info',
            'conditions': 'is_going_to_state_detail_info'
        },
		{
            'trigger': 'advance',
            'source': 'state_ticket_prcie',
            'dest': 'state_price1',
            'conditions': 'is_going_to_state_price1'
        },
		{
            'trigger': 'advance',
            'source': 'state_ticket_prcie',
            'dest': 'state_price2',
            'conditions': 'is_going_to_state_price2'
        },
		{
            'trigger': 'advance',
            'source': 'state_ticket_prcie',
            'dest': 'state_price3',
            'conditions': 'is_going_to_state_price3'
        },
		{
            'trigger': 'advance',
            'source': 'state_price1',
            'dest': 'state_buy',
            'conditions': 'is_going_to_state_buy'
        },
		{
            'trigger': 'advance',
            'source': 'state_price2',
            'dest': 'state_buy',
            'conditions': 'is_going_to_state_buy'
        },
		{
            'trigger': 'advance',
            'source': 'state_price3',
            'dest': 'state_buy',
            'conditions': 'is_going_to_state_buy'
        },
		{
            'trigger': 'advance',
            'source': 'state_sponsor',
            'dest': 'state_transfer',
            'conditions': 'is_going_to_state_transfer'
        },
		{
            'trigger': 'advance',
            'source': 'state_transfer',
            'dest': 'state_sponsor1000',
            'conditions': 'is_going_to_state_sponsor1000'
        },
		{
            'trigger': 'advance',
            'source': 'state_transfer',
            'dest': 'state_sponsor5000',
            'conditions': 'is_going_to_state_sponsor5000'
        },
		{
            'trigger': 'advance',
            'source': 'state_transfer',
            'dest': 'state_sponsor10000',
            'conditions': 'is_going_to_state_sponsor10000'
        },		
		{
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state_crew_list',
            'conditions': 'is_going_to_state_crew_list'
        },	
        {
            'trigger': 'go_back',
            'source': [
                'state_session',
                'state_ticket_prcie',
				'state_sponsor',
				'state_transfer',
				'state_Jan',
				'state_Feb',
				'state_March',
				'state_price1',
				'state_price2',
				'state_price3',
				'state_buy',
				'state_sponsor1000',
				'state_sponsor5000',
				'state_sponsor10000',
				'state_crew_list',
				'state_detail_info'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="localhost", port=5000, debug=True, reloader=True)
