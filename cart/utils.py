import threading
from django.core.mail import send_mail
from django.conf import settings


def send_purchase_email(user_email, book_list):
    subject = 'Purchase Confirmation'
    message = f'Thank you for your purchase. You have bought the following books: {book_list}'
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, from_email, [user_email])


def send_purchase_email_async(user_email, book_list):
    print('*****')
    threading.Thread(target=send_purchase_email, args=(user_email, book_list)).start()
