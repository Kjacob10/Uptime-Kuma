from twilio.rest import Client

def send_call_alert(phone_number, message):
    account_sid = 'ACf4b1ffbd2b85230d94f416aaf9fd36c0'
    auth_token = '7f65af01c3f09b0baf0b48ea7e6403dd'
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        to=phone_number,
        from_='+12084860252',
        twiml=f'<Response><Say>{"This is an alert message"}</Say></Response>'
    )
    print(f"Call sent to {phone_number}, SID: {call.sid}")

if __name__ == "__main__":
    send_call_alert('+919359461477', 'Server is down! Please check immediately.')
