# import smtplib
# import sys
 


# from flask.views import MethodView
# from flask import Flask, jsonify, render_template, request
# import json
# import os

# from twilio.rest import Client





# class SMSView():
#     def __init__(self):...
#     def send_twilo(self, message, to_number):
#         # Your Twilio credentials
     
       
#         client = Client(account_sid, auth_token)

#         # Create a Twilio client

#         try:
#             message = client.messages.create(
#                 body=message,
#                 from_=twilio_number,
#                 to=to_number
#             )
#             print(f"Message sent! SID: {message.sid}")
#         except Exception as e:
#             print(f"An error occurred: {e}")
#     def send_message(self, phone_number, carrier, message):
#         CARRIERS = {
#             "att": "@mms.att.net",
#             "tmobile": "@tmomail.net",
#             "verizon": "@vtext.com",
#             "sprint": "@messaging.sprintpcs.com"
#         }
        
#         EMAIL = "EMAIL"
#         PASSWORD = "PASSWORD"
#         recipient = phone_number + CARRIERS[carrier]
#         auth = (EMAIL, PASSWORD)
    
#         server = smtplib.SMTP("smtp.gmail.com", 587)
#         server.starttls()
#         server.login(auth[0], auth[1])
    
#         server.sendmail(auth[0], recipient, message)
#     def post(self):
#         pass
       
        

# # SMS_VIEW = SMSView.as_view("sms_view")


# # Example usage
# # if __name__ == "__main__":
# #     recipient_number = '+639958466656'  # Replace with the recipient's number
# #     sms_message = 'Hello! This is a test message from Python.'
# #     sms = SMSView()
# #     sms.send_twilo(sms_message, recipient_number)