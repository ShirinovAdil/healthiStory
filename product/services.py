from django.core.mail import send_mail
from django.conf import settings


def mobile_station_order_send_mail(**kwargs):
    """Send mail to user with order information"""
    email_from = settings.EMAIL_HOST_USER
    subject = "Healthistory Order"
    message = f"Thanks {kwargs['name']} for ur order." \
              f"You will get station_amount {kwargs['station_amount']}" \
              f"You will get capacity_number {kwargs['capacity_number']}" \
              f"You will get card_number {kwargs['card_number']}" \
              f"You will get lancet_number {kwargs['lancet_number']}" \
              f"You will get glucose_number {kwargs['glucose_number']}" \
              f"You will get ketone_number {kwargs['ketone_number']}" \
              f"You will get panel_number {kwargs['panel_number']}" \
              f"You will get cholesterol_number {kwargs['cholesterol_number']}" \
              f"You will get acid_number {kwargs['acid_number']}" \
              f"You will get creatinine_number {kwargs['creatinine_number']}"
    recipient_list = [kwargs['email'],]

    send_mail(subject, message, email_from, recipient_list)
