from twilio.rest import Client

def send_call_alert(phone_number, message):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        to=phone_number,
        from_='your_twilio_number',
        twiml=f'<Response><Say>{"This is an alert message"}</Say></Response>'
    )
    print(f"Call sent to {phone_number}, SID: {call.sid}")

if __name__ == "__main__":
    send_call_alert('verified_phone_number_to_recieve_message', 'Server is down! Please check immediately.')
