from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACd15f4f042f502baaf2f0377aab6c4be7"
auth_token  = "8f6a12a6bef7a55ab09b63d6fef38965"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(
    body="Testing the message app",
    to="+972527514302",    # Replace with your phone number
    from_="+441274451632") # Replace with your Twilio number
print message.sid
