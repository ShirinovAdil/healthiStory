from django.core.mail import send_mail
from django.conf import settings


def mobile_station_order_send_mail(**kwargs):
    """Send mail to user with order information"""
    email_from = settings.EMAIL_HOST_USER
    subject = "Healthistory Order"
    message = f"""
              Sender {kwargs['email']}
              Name of sender {kwargs['name']}
              Phone: {kwargs['phone']}
              Address: {kwargs['address']}
______________________________________

              You will get station_amount:      {kwargs['station_amount']}
              You will get capacity_number:     {kwargs['capacity_number']}
              You will get card_number:         {kwargs['card_number']}
              You will get lancet_number:       {kwargs['lancet_number']}
              You will get glucose_number:      {kwargs['glucose_number']}
              You will get ketone_number:       {kwargs['ketone_number']}
              You will get panel_number:        {kwargs['panel_number']}
              You will get cholesterol_number:  {kwargs['cholesterol_number']}
              You will get acid_number:         {kwargs['acid_number']}
              You will get creatinine_number:   {kwargs['creatinine_number']}"""
    if kwargs['station_amount'] or kwargs['capacity_number'] or kwargs['card_number'] or kwargs['lancet_number'] or kwargs['glucose_number'] or kwargs['ketone_number'] or kwargs['panel_number'] or kwargs['cholesterol_number'] or kwargs['acid_number'] or kwargs['creatinine_number']:
        recipient_list = ['eocaqverdiyev@std.beu.edu.az']
        send_mail(subject, message, email_from, recipient_list)
        return 1
    else:
        return 0
