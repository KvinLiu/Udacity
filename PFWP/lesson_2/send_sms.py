from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACceddc19b9e8b7cc6b4773a3f929908a9"
auth_token  = "a7fbd466cd522f5f6731267243ed93f2"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="Hi, I am Kevin?",
    to="+12503950791",    # Replace with your phone number
    from_="+15878050771") # Replace with your Twilio number
print message.sid
