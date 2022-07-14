from concurrent.futures import thread
import email
from email import message
import threading
from django.conf import settings 
from django.core.mail import send_mail
from sympy import re



class SendAccountActivationEmail(threading.Thread):
    def __init__(self, email , token):
        self.email = email 
        self.token = token 
        threading.Thread.__init__(self)

    
    def run(self):
        try:
            subject = "لینک تایید ایمیل شما"
            message = f'{settings.BASE_URL}/api/accounts/verify/{self.token}/ فعال کنید سلام. لطفا روی لینک زیر کلیک کنیدتا پسورد خودتون رو در آدرس '
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [self.email]
            send_mail(subject, message, email_from, recipient_list)

        except Exception as e:
            print(e)


    

class SendForgetPasswordEmail(threading.Thread):
    def __init__(self, email, token):
        self.email = email
        self.token = token
        threading.Thread.__init__(self)

    def run(self, email, token):
        try:
            subject = 'لینک بازگشایی ایمیل شما'
            message = f' {settings.BASE_UTL}api/accounts/change-password/{self.token}/ سلام. روی لینک زیر کلیک کنید تا پسورد خود را بازگشایی کنید '
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [self.email]
            send_mail(subject, message, email_from, recipient_list)
        
        except Exception as e:
            print(e)


