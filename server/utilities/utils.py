from django.core.mail import send_mail
from django.conf import settings


def send_email(
    subject,
    plain_message,
    html_content,
    to_email,
):
    send_mail(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        to_email,
        html_message=html_content,
    )
    return "Done"
