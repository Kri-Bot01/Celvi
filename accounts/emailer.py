from django.core.mail import send_mail
from django.conf import settings


def signup_success_email(user_name,to_address):
    subject = "Congratulations! Welcome to Celvi"
    message = f"Dear {user_name},\n\nCongratulations on successfully signing up with Celvi! We are thrilled to have you on board. Regards Celvi Team"
    send_mail(
    subject,
    message,
    settings.EMAIL_HOST_USER,
    [to_address],
    fail_silently=False,
)